from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from apps.api.serializers.users import UserDTO
from apps.users.models import User


# Бизнес-логика для создания пользователя
def create_user(user: "UserDTO") -> "UserDTO":
    if User.objects.filter(email=user.email).exists():
        raise ValidationError(
            {
                "message": "This email is already in use.",
                "code": "user_already_exists",
            }
        )

    try:
        instance = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )

        if user.password:
            instance.set_password(user.password)
        instance.save()
        return UserDTO.from_instance(instance)
    except IntegrityError:
        raise ValidationError(
            {
                "message": "This email is already in use.",
                "code": "user_already_exists",
            }
        )
