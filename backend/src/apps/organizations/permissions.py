from rest_framework.permissions import BasePermission

from apps.organizations.models import Membership


# Класс HasPermissions проверяет, есть ли у пользователя необходимые права для доступа к представлению.
class HasPermissions(BasePermission):
    def has_permission(self, request, view):
        organization_id = view.kwargs.get("organization_id")
        if not organization_id:
            return False

        membership = Membership.objects.filter(
            user=request.user.id, organization_id=organization_id
        ).first()
        if not membership:
            return False

        required_permissions = getattr(view, "required_permissions", None)
        if required_permissions is None:
            return False

        return membership.has_permission(required_permissions)


# Класс HasRole проверяет, есть ли у пользователя необходимая роль для доступа к представлению.
class HasRole(BasePermission):
    def has_permission(self, request, view):
        organization_id = view.kwargs.get("organization_id")
        if not organization_id:
            return False

        membership = Membership.objects.filter(
            user=request.user.id, organization_id=organization_id
        ).first()
        if not membership:
            return False

        required_role = getattr(view, "required_role", None)
        if required_role is None:
            return False

        return membership.role_id == required_role
