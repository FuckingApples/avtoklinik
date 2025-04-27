import { env } from "~/env";

export const PROVIDERS = {
  yandex: {
    client_id: env.NEXT_PUBLIC_YANDEX_CLIENT_ID,
    auth_url: "https://oauth.yandex.ru/authorize",
    scopes: "login:email login:info",
    optional_scopes: "login:avatar",
  },
  vk: {
    client_id: env.NEXT_PUBLIC_VK_CLIENT_ID,
    auth_url: "https://id.vk.com/authorize",
    scopes: "login:email login:info",
    optional_scopes: null,
  },
} as const;
