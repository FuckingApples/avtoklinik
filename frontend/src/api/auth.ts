import type { TSignInSchema, TSignUpSchema } from "~/utils/validation/auth";
import type { TEmailVerificationSchema } from "~/utils/validation/email-verification";
import api from "~/lib/axios";

export async function registerUser(data: Omit<TSignUpSchema, "re_password">) {
  return api
    .post<RegisterResponse>("/v1/user/register", data)
    .then((res) => res.data);
}

export async function loginUser(data: TSignInSchema) {
  return api.post<LoginResponse>("/token", data).then((res) => res.data);
}

export async function logoutUser() {
  return api.post("/v1/user/logout");
}

export async function requestEmailVerification() {
  return api.get("/v1/user/email/verify/get_otp");
}

export async function sendEmailVerification(data: TEmailVerificationSchema) {
  return api.post<void>("/v1/user/email/verify", data).then((res) => res.data);
}

export type LoginResponse = {
  access: string;
  is_email_verified: boolean;
};

export type RegisterResponse = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
};
