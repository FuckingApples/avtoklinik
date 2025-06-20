import base64
import os
from datetime import datetime, timedelta

import requests
from django.urls import path
from rest_framework import permissions, status, views, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.api.serializers.oauth import (
    OAuthProviderSerializer,
    OAuthSerializer,
    VKOAuthSerializer,
)
from apps.oauth.models import OAuthProvider
from apps.users.models import User
from core.settings import (
    OAUTH_VK_CLIENT_ID,
    OAUTH_YANDEX_CLIENT_ID,
    OAUTH_YANDEX_CLIENT_SECRET,
)


class OAuthProviderViewSet(viewsets.ModelViewSet):
    serializer_class = OAuthProviderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return OAuthProvider.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class YandexOAuthAPI(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = OAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        # Запрашиваем токен у Яндекса
        token_obtain_url = "https://oauth.yandex.ru/token"
        auth_token = base64.b64encode(
            f"{OAUTH_YANDEX_CLIENT_ID}:{OAUTH_YANDEX_CLIENT_SECRET}".encode()
        ).decode()
        data = {
            "grant_type": "authorization_code",
            "code": validated_data["code"],
            "code_verifier": validated_data["code_verifier"],
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {auth_token}",
        }

        token_response = requests.post(token_obtain_url, data=data, headers=headers)

        if token_response.status_code != 200:
            return Response(
                {
                    "code": token_response.json().get("error"),
                    "message": token_response.json().get("error_description"),
                },
                status=token_response.status_code,
            )

        access_token = token_response.json().get("access_token")

        # Получаем информацию о пользователе
        user_info_url = "https://login.yandex.ru/info"
        headers = {"Authorization": f"OAuth {access_token}"}
        user_response = requests.get(user_info_url, headers=headers)

        if user_response.status_code != 200:
            return Response(
                {
                    "code": "yandex_user_token_error",
                    "message": "Something went wrong while getting user info",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_data = user_response.json()
        email = user_data.get("default_email")
        first_name = user_data.get("first_name")
        last_name = user_data.get("last_name")
        uid = user_data.get("psuid")

        is_avatar_empty = user_data.get("is_avatar_empty", True)
        default_avatar_id = user_data.get("default_avatar_id", None)

        if not email:
            return Response(
                {"code": "no_email", "message": "No email provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not last_name and not first_name:
            return Response(
                {"code": "no_name", "message": "No name provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Регистрация/авторизация пользователя
        social_account = OAuthProvider.objects.filter(
            provider="yandex", uid=uid
        ).first()

        if social_account:
            user = social_account.user
        else:
            # Проверяем зарегистрирован ли уже пользователь с таким email
            user = User.objects.filter(email=email).first()
            if user:
                return Response(
                    {
                        "code": "account_not_connected",
                        "message": "Email already exists and this account not connected",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = User.objects.create(
                email=email, last_name=last_name, first_name=first_name
            )
            user.set_unusable_password()
            user.is_email_verified = True
            if default_avatar_id and not is_avatar_empty:
                user.avatar = f"https://avatars.yandex.net/get-yapic/{default_avatar_id}/islands-200"
            user.save()
            OAuthProvider.objects.create(user=user, provider="yandex", uid=uid)

        # Генерация JWT токенов
        refresh_token = RefreshToken.for_user(user)
        response = Response(
            {"access": str(refresh_token.access_token), "refresh": str(refresh_token)},
            status=status.HTTP_200_OK,
        )
        response.set_cookie(
            "refresh",
            str(refresh_token),
            httponly=True,
            secure=True,
            domain="." + os.getenv("BASE_DOMAIN", ""),
            samesite="None",
            path="/",
            expires=datetime.now() + timedelta(days=30),
        )
        return response


class VKOAuthAPI(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = VKOAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        # Запрашиваем токен у ВКонтакте
        token_obtain_url = "https://id.vk.com/oauth2/auth"
        data = {
            "grant_type": "authorization_code",
            "code": validated_data["code"],
            "code_verifier": validated_data["code_verifier"],
            "client_id": OAUTH_VK_CLIENT_ID,
            "device_id": validated_data["device_id"],
            # "redirect_uri": validated_data["redirect_uri"], TODO: Uncomment before push
            "redirect_uri": "http://localhost/api/oauth",
        }

        token_response = requests.post(token_obtain_url, data=data)

        if token_response.json().get("error"):
            return Response(
                {
                    "code": token_response.json().get("error"),
                    "message": token_response.json().get("error_description"),
                },
                status=token_response.status_code,
            )

        access_token = token_response.json().get("access_token")

        # Получаем информацию о пользователе
        user_info_url = "https://id.vk.com/oauth2/user_info"
        data = {"client_id": OAUTH_VK_CLIENT_ID, "access_token": access_token}
        user_response = requests.post(user_info_url, data=data)


urlpatterns = [
    path("yandex/", YandexOAuthAPI.as_view(), name="yandex_oauth"),
    path("vk/", VKOAuthAPI.as_view(), name="vk_oauth"),
]
