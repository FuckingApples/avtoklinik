import api from "~/lib/axios";
import type { TOrganizationCreationSchema } from "~/utils/validation/organization-creation";
import type { Organization } from "~/types/organization";

export async function getOrganizationInfo(id: number) {
  return api
    .get<Organization>(`/v1/organizations/${id}`)
    .then((res) => res.data);
}

export async function createOrganization(data: TOrganizationCreationSchema) {
  return api
    .post<Organization>("/v1/organizations/", data)
    .then((res) => res.data);
}
