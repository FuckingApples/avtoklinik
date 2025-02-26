from datetime import datetime, timedelta

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer


class CustomTokenObtainPairAPI(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        browser_keywords = ["Mozilla/5.0", "Chrome", "Safari", "Firefox"]
        is_mobile = not any(
            kw in request.headers.get("User-Agent", "") for kw in browser_keywords
        )
        response.data["is_email_verified"] = response.data.get(
            "is_email_verified", False
        )
        if is_mobile:
            return response
        refresh_token = response.data.pop("refresh", None)
        if refresh_token:
            response.set_cookie(
                "refresh",
                refresh_token,
                httponly=True,
                secure=True,
                samesite="None",
                path="/",
                expires=datetime.now() + timedelta(days=30),
            )

        return response


class CustomTokenRefreshAPI(TokenRefreshView):
    @method_decorator(csrf_protect)
    def post(self, request: Request, *args, **kwargs) -> Response:
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
                status=HTTP_400_BAD_REQUEST,
            )

        serializer = TokenRefreshSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        response = Response(data=serializer.validated_data, status=HTTP_200_OK)
        if not is_mobile:
            new_refresh_token = serializer.validated_data.pop("refresh", None)
            if new_refresh_token:
                response.set_cookie(
                    "refresh",
                    new_refresh_token,
                    httponly=True,
                    secure=True,
                    samesite="None",
                    path="/",
                    expires=datetime.now() + timedelta(days=30),
                )

        return response
