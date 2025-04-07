import uuid
from typing import Optional

from django.db import models

from apps.core.models import SafeDeleteManager, SoftDeleteModel
from apps.users.models import User


# Модель организации
# Поля:
# - public_id - уникальный публичный идентификатор организации
# - name - название организации
# - created_at - дата создания
# - is_deleted - флаг удаления
# - deleted_at - дата удаления
class Organization(SoftDeleteModel):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = SafeDeleteManager()
    all_objects = models.Manager()

    # Метод для получения роли пользователя в организации
    def get_user_role(self, user: "User") -> Optional[str]:
        if not user.is_authenticated:
            return None

        membership = (
            self.membership_set.filter(user=user).select_related("role").first()
        )
        return membership.role if membership else None

    def __str__(self):
        return self.name


# Флаги разрешений в битовом формате
class PermissionFlags:
    MANAGE_ORGANIZATION = 1 << 0
    INVITE_USERS = 1 << 1

    PERMISSION_CHOICES = [
        (MANAGE_ORGANIZATION, "Manage organization"),
        (INVITE_USERS, "Invite users"),
    ]


# Роли пользователей в организации
class Role(models.TextChoices):
    OWNER = "owner", "Владелец"
    ADMIN = "admin", "Администратор"
    MANAGER = "manager", "Менеджер"
    STAFF = "staff", "Сотрудник"


# Словарь с разрешениями по умолчанию для каждой роли
DEFAULT_PERMISSIONS = {
    Role.OWNER: list(range(0, 63)),
    Role.ADMIN: [],
    Role.MANAGER: [],
    Role.STAFF: [],
}


# Менеджер для модели Membership с фильтрацией по is_deleted организации
class MembershipManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(organization__is_deleted=False)


# Модель членства в организации
# Поля:
# - user - пользователь
# - organization - организация
# - role - роль пользователя в организации
# - permissions - разрешения пользователя в организации
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memberships")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STAFF,
    )
    permissions = models.PositiveBigIntegerField(blank=True, default=0)

    objects = MembershipManager()
    all_objects = models.Manager()

    class Meta:
        unique_together = ("user", "organization")

    # Метод для проверки разрешения пользователя
    def has_permission(self, permission):
        return (self.permissions & permission) == permission

    # Метод для добавления разрешения пользователю
    def add_permission(self, permission):
        self.permissions |= permission
        self.save()

    # Метод для удаления разрешения у пользователя
    def remove_permission(self, permission):
        self.permissions &= ~permission
        self.save()

    # Метод для получения разрешений пользователя в читаемом формате для админки
    def get_permissions_display(self):
        return [
            permission
            for bit, permission in PermissionFlags.PERMISSION_CHOICES
            if self.has_permission(bit)
        ]

    def __str__(self):
        return f"{self.user} - {self.organization} ({self.permissions})"
