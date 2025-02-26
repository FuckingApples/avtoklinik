import uuid

from django.db import models
from django.utils import timezone

from apps.users.models import User


class OrganizationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Organization(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = OrganizationManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name


class PermissionFlags:
    MANAGE_ORGANIZATION = 1 << 0
    INVITE_USERS = 1 << 1

    PERMISSION_CHOICES = [
        (MANAGE_ORGANIZATION, "Manage organization"),
        (INVITE_USERS, "Invite users"),
    ]

    # TODO: Сделать флаг OWNER на 64 бит при переходе на прод (PostgresSQL)
    OWNER = 1 << 62 | MANAGE_ORGANIZATION | INVITE_USERS


class MembershipManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(organization__is_deleted=False)


class Membership(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    permission = models.PositiveBigIntegerField(default=0)

    objects = MembershipManager()
    all_objects = models.Manager()

    class Meta:
        unique_together = ("user", "organization")

    def has_permission(self, permission):
        return (self.permission & permission) == permission

    def add_permission(self, permission):
        self.permission |= permission
        self.save()

    def remove_permission(self, permission):
        self.permission &= ~permission
        self.save()

    def get_permissions_display(self):
        return [
            permission
            for bit, permission in PermissionFlags.PERMISSION_CHOICES
            if self.has_permission(bit)
        ]

    def __str__(self):
        return f"{self.user} - {self.organization} ({self.permission})"
