from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        if "Mobile" in request.headers.get("User-Agent", ""):
            return response
        refresh_token = response.data.pop("refresh", None)
        if refresh_token:
            response.set_cookie(
                "refresh",
                refresh_token,
                httponly=True,
                secure=True,
                samesite="Strict",
                path="/api/token/refresh",
            )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        data = request.data.copy()
        is_mobile = "Mobile" in request.headers.get("User-Agent", "")
        if not is_mobile:
            refresh_token = request.COOKIES.get("refresh")
            if refresh_token:
                data["refresh"] = refresh_token

        if "refresh" not in data or not data["refresh"]:
            return Response(
                {"error": "Refresh token not found"}, status=HTTP_400_BAD_REQUEST
            )

        serializer = TokenRefreshSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)

        response = Response(data=serializer.validated_data, status=HTTP_200_OK)
        if not is_mobile:
            new_refresh_token = serializer.validated_data.pop("refresh", None)
            if new_refresh_token:
                response.set_cookie(
                    "refresh",
                    new_refresh_token,
                    httponly=True,
                    secure=True,
                    samesite="Strict",
                    path="/api/token/refresh",
                )

        return response
