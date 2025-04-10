from rest_framework.permissions import BasePermission

from apps.organizations.services.organizations import build_permission_mask


# TODO: Think about base class
# Класс HasPermissions проверяет, есть ли у пользователя необходимые права для доступа к представлению.
class HasPermissions(BasePermission):
    required_permissions = {}

    def has_permission(self, request, view):
        user = request.user
        organization_id = view.kwargs.get("organization_id")
        method = request.method.upper()

        if not organization_id:
            return False

        membership = user.memberships.filter(organization_id=organization_id).first()
        if not membership:
            return False

        required_permissions = getattr(view, "required_permissions", {}).get(method, [])
        if isinstance(required_permissions, list):
            required_permissions = build_permission_mask(required_permissions)

        return membership.has_permission(required_permissions)


# Класс HasRole проверяет, есть ли у пользователя необходимая роль для доступа к представлению.
class HasRole(BasePermission):
    required_roles = {}

    def has_permission(self, request, view):
        user = request.user
        organization_id = view.kwargs.get("organization_id")
        method = request.method.upper()

        if not organization_id:
            return False

        membership = user.memberships.filter(organization_id=organization_id).first()
        if not membership:
            return False

        allowed_roles = getattr(view, "required_roles", {}).get(method, [])
        if allowed_roles and membership.role not in allowed_roles:
            return False

        return True
