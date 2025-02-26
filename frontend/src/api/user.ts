import api from "~/lib/axios";

export async function getUserInfo() {
  return api.get<GetUserInfo>("/v1/user").then((res) => res.data);
}

export type GetUserInfo = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  is_email_verified: boolean;
  organizations: GetOrganizationInfo[];
};

// TODO: move to organization api file
export type GetOrganizationInfo = {
  id: number;
  public_id: string;
  name: string;
};
