import api from "~/lib/axios";
import type { User } from "~/types/user";
import type { TSignUpSchema } from "~/utils/validation/auth";
import type { TUserSettingsSchema } from "~/utils/validation/user-settings";

export async function getUserInfo() {
  return api.get<User>("/v1/user/").then((res) => res.data);
}

export async function createUser(data: Omit<TSignUpSchema, "re_password">) {
  return api
    .post<Omit<User, "organizations" | "is_email_verified">>("/v1/user/", data)
    .then((res) => res.data);
}

export async function updateUser(
  data: Partial<Omit<TUserSettingsSchema, "re_password">>,
) {
  return api.patch<User>(`/v1/user/`, data).then((res) => res.data);
}
