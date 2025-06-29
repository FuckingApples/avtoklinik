from django.db import IntegrityError

from apps.core.exceptions import DetailedValidationException
from apps.users.models import User


# Бизнес-логика для создания пользователя
def create_user(user: "User"):
    if User.objects.filter(email=user["email"]).exists():
        raise DetailedValidationException(
            message="This email is already in use.", code="user_already_exists"
        )

    try:
        instance = User(
            first_name=user["first_name"],
            last_name=user["last_name"],
            email=user["email"],
        )

        if user["password"]:
            instance.set_password(user["password"])
        instance.save()
        return instance
    except IntegrityError:
        raise DetailedValidationException(
            message="This email is already in use.", code="user_already_exists"
        )
