import api from "~/lib/axios";
import type { TOrganizationCreationSchema } from "~/utils/validation/organization-creation";
import type { Organization } from "~/types/organization";

export async function getNumericOrgId(uuidOrgId: string): Promise<number> {
  try {
    const response = await api.get<Organization[]>(`/v1/organizations/`, {
      params: { uuid: uuidOrgId }
    });
    
    const matchingOrg = response.data.find(org => org.public_id === uuidOrgId);
    
    if (matchingOrg?.id) {
      return matchingOrg.id;
    }
    
    throw new Error(`Organization with uuid ${uuidOrgId} not found`);
  } catch (error) {
    throw new Error(`Organization with uuid ${uuidOrgId} not found`);
  }
}

export async function createOrganization(data: TOrganizationCreationSchema) {
  return api
    .post<Organization>("/v1/organizations/", data)
    .then((res) => res.data);
}
