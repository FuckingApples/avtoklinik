import type { TSignInSchema, TSignUpSchema } from "~/utils/validation/auth";
import api from "~/lib/axios";

export async function registerUser(data: Omit<TSignUpSchema, "re_password">) {
  return api.post("/v1/users/register", data).then((res) => res.data);
}

export async function loginUser(data: TSignInSchema) {
  return api.post("/token", data).then((res) => res.data);
}

export async function logoutUser() {
  return api.post("/v1/users/logout");
}
