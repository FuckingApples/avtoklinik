from apps.api.serializers.users import UserDTO
from apps.users.models import User


def create_user(user: "UserDTO") -> "UserDTO":
    instance = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )

    if user.password:
        instance.set_password(user.password)
    instance.save()
    return UserDTO.from_instance(instance)
