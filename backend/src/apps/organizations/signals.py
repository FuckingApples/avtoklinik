from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.organizations.models import DEFAULT_PERMISSIONS, Membership
from apps.organizations.services.organizations import build_permission_mask


@receiver(post_save, sender=Membership)
def assign_default_permissions(sender, instance, created, **kwargs):
    if created:
        default_permissions = DEFAULT_PERMISSIONS.get(instance.role, [])
        instance.permissions = build_permission_mask(default_permissions)
        instance.save()
