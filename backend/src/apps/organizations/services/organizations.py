from typing import TYPE_CHECKING

from apps.api.serializers.organizations import OrganizationDTO
from apps.organizations.models import Organization, Membership, PermissionFlags, Role

if TYPE_CHECKING:
    from apps.users.models import User


# Бизнес-логика для создания организациями
def create_organization(organization: "OrganizationDTO", user: "User"):
    instance = Organization.objects.create(name=organization.name)

    Membership.objects.create(organization=instance, user=user, role=Role.OWNER)

    return OrganizationDTO.from_instance(instance)


# Бизнес-логика для удаления организации
def delete_organization(organization_id: int):
    instance = Organization.objects.get(id=organization_id, is_deleted=False)

    instance.soft_delete()


def build_permission_mask(bits: list[int]) -> int:
    """
    Создает битовую маску разрешений на основе списка битов. Пример: [0, 1, 2] -> 0b111
    """
    mask = 0
    for bit in bits:
        mask |= 1 << bit
    return mask
