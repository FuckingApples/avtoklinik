import type { TSignInSchema } from "~/utils/validation/auth";
import type { TEmailVerificationSchema } from "~/utils/validation/email-verification";
import api from "~/lib/axios";
import type { LoginResponse, OAuthResponse } from "~/types/api";

export async function loginUser(data: TSignInSchema) {
  return api.post<LoginResponse>("/token/", data).then((res) => res.data);
}

export async function logoutUser() {
  return api.post("/v1/user/logout/");
}

export async function requestEmailVerification() {
  return api.get("/v1/user/email/verify/get_otp/");
}

export async function sendEmailVerification(data: TEmailVerificationSchema) {
  return api.post<void>("/v1/user/email/verify/", data).then((res) => res.data);
}

export async function yandexOAuth(code: string) {
  return api
    .post<OAuthResponse>("/v1/oauth/yandex/", { code })
    .then((res) => res.data);
}
