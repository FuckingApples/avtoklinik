import uuid
from typing import Optional

from django.db import models
from django.utils import timezone

from apps.users.models import User


# Менеджер для модели Organization с фильтрацией по is_deleted
class OrganizationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


# Модель организации
# Поля:
# - public_id - уникальный публичный идентификатор организации
# - name - название организации
# - created_at - дата создания
# - is_deleted - флаг удаления
# - deleted_at - дата удаления
class Organization(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = OrganizationManager()
    all_objects = models.Manager()

    # Метод для мягкого удаления организации (помечает организацию как удаленную)
    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # Метод для восстановления организации
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    # Метод для получения роли пользователя в организации
    def get_user_role(self, user: "User") -> Optional[str]:
        if not user.is_authenticated:
            return None

        membership = (
            self.membership_set.filter(user=user).select_related("role").first()
        )
        return membership.role.name if membership else None

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


# Модель роли
# Поля:
# - name - название роли
# - default_permissions - разрешения по умолчанию
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    default_permissions = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name


# Менеджер для модели Membership с фильтрацией по is_deleted организации
class MembershipManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(organization__is_deleted=False)


# Модель членства в организации
# Поля:
# - user - пользователь
# - organization - организация
# - role - роль пользователя в организации
# - custom_permissions - пользовательские разрешения
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    custom_permissions = models.PositiveBigIntegerField(null=True, blank=True)

    objects = MembershipManager()
    all_objects = models.Manager()

    class Meta:
        unique_together = ("user", "organization")

    # Метод для получения разрешений пользователя
    @property
    def permissions(self):
        return (
            self.custom_permissions
            if self.custom_permissions is not None
            else self.role.default_permissions
        )

    # Метод для проверки разрешения пользователя
    def has_permission(self, permission):
        return (self.permissions & permission) == permission

    # Метод для добавления разрешения пользователю
    def add_permission(self, permission):
        self.custom_permissions |= permission
        self.save()

    # Метод для удаления разрешения у пользователя
    def remove_permission(self, permission):
        self.custom_permissions &= ~permission
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
