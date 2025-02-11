from rest_framework.response import Response
from rest_framework.views import APIView
from apps.api.serializers.users import UserSerializer
from apps.users.services import create


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        print(data)
        serializer.instance = create.create_user(user=data)

        return Response(data=serializer.data)
