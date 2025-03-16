import api from "~/lib/axios";
import type { TOrganizationCreationSchema } from "~/utils/validation/organization-creation";
import type { Organization } from "~/types/organization";

export async function createOrganization(data: TOrganizationCreationSchema) {
  return api
    .post<Organization>("/v1/organization/create/", data)
    .then((res) => res.data);
}
