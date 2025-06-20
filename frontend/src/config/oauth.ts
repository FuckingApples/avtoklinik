import { env } from "~/env";

export const PROVIDERS = {
  yandex: {
    client_id: env.NEXT_PUBLIC_YANDEX_CLIENT_ID,
    auth_url: "https://oauth.yandex.ru/authorize",
    scopes: "login:email login:info",
    optional_scopes: "login:avatar",
    required_params: ["code"],
    optional_params: [
      "client_id",
      "client_secret",
      "device_id",
      "device_name",
      "code_verifier",
    ],
  },
  vk: {
    client_id: env.NEXT_PUBLIC_VK_CLIENT_ID,
    auth_url: "https://id.vk.com/authorize",
    scopes: "vkid.personal_info email",
    optional_scopes: null,
    required_params: [
      "code",
      "code_verifier",
      "client_id",
      "device_id",
      "redirect_uri",
    ],
    optional_params: ["state"],
  },
  alfabank: {
    client_id: env.NEXT_PUBLIC_ALFABANK_CLIENT_ID,
    auth_url: "https://id-sandbox.alfabank.ru/oidc/authorize",
    scopes: "openid profile email",
    optional_scopes: null,
    required_params: ["code", "client_id", "client_secret", "redirect_uri"],
    optional_params: ["code_verifier"],
  },
} as const;
