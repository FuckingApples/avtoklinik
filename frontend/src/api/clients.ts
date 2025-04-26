import api from "~/lib/axios";
import { getNumericOrgId } from "~/api/organization";

export interface Client {
  id: string;
  first_name: string;
  last_name: string;
  middle_name?: string;
  phone: string;
  email?: string;
  created_at: string;
  updated_at: string;
}

export async function getClients(orgId: string) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api.get<Client[]>(`/v1/organizations/${numericOrgId}/clients/`).then((res) => res.data);
}
