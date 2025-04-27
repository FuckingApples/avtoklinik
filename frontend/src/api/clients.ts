import api from "~/lib/axios";

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

export async function getClients(orgId: number) {
  return api.get<Client[]>(`/v1/organizations/${orgId}/clients/`).then((res) => res.data);
}
