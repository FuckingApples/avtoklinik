from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.api.serializers.users import RegisterUserSerializer, UserInfoSerializer
from apps.users.services import users


class RegisterUserAPI(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = users.create_user(user=data)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserInfoAPI(APIView):
    def get(self, request):
        serializer = UserInfoSerializer(request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LogoutUserAPI(APIView):
    def post(self, request: Request):
        data = request.data.copy()
        browser_keywords = ["Mozilla/5.0", "Chrome", "Safari", "Firefox"]
        is_mobile = not any(
            kw in request.headers.get("User-Agent", "") for kw in browser_keywords
        )
        if not is_mobile:
            refresh_token = request.COOKIES.get("refresh")
            if refresh_token:
                data["refresh"] = refresh_token

        if "refresh" not in data or not data["refresh"]:
            return Response(
                {"code": "token_not_found", "message": "Refresh token not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            refresh_token = RefreshToken(data["refresh"])
            refresh_token.blacklist()
            response = Response(status=status.HTTP_205_RESET_CONTENT)
            response.delete_cookie("refresh")
            return response
        except TokenError:
            return Response(
                {"code": "token_invalid", "message": "Invalid refresh token"},
                status=status.HTTP_400_BAD_REQUEST,
            )
