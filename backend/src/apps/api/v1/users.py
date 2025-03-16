from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions, views
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.api.serializers.users import UserSerializer, UserDTO
from apps.users.services import users


@extend_schema(tags=["Users"])
@extend_schema_view(
    post=extend_schema(
        summary="Регистрация пользователя",
        request=UserSerializer,
        responses={status.HTTP_201_CREATED: UserSerializer},
        auth=[],
    ),
    get=extend_schema(
        summary="Получение информации о текущем пользователе",
        responses={status.HTTP_200_OK: UserSerializer},
    ),
)
class UserAPI(views.APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def get(self, request):
        serializer = UserSerializer(request.user, context={"request": request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = UserDTO(**serializer.validated_data)
        serializer.instance = users.create_user(user=data)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        serializer = UserSerializer(
            instance=request.user,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["Users"])
class LogoutUserAPI(views.APIView):
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
