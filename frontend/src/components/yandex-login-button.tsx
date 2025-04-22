"use client";

import { useEffect } from "react";
import { useTheme } from "next-themes";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import { env } from "~/env";

declare global {
  interface Window {
    YaAuthSuggest?: {
      init: (
        options: {
          client_id: string;
          response_type: string;
          redirect_uri: string;
          optional_scope?: string;
        },
        url: string,
        buttonOptions: {
          view: string;
          parentId: string;
          buttonSize: string;
          buttonView: string;
          buttonTheme: string;
          buttonBorderRadius: string;
          buttonIcon: string;
        },
      ) => Promise<{
        handler: () => Promise<{ access_token: string; expires_in: number }>;
      }>;
    };
  }
}

export const YandexLoginButton = () => {
  const { theme = "dark", systemTheme } = useTheme();
  const router = useRouter();

  const resolvedTheme = theme === "system" ? systemTheme : theme;

  useEffect(() => {
    if (
      typeof window !== "undefined" &&
      window.YaAuthSuggest &&
      resolvedTheme
    ) {
      window.YaAuthSuggest.init(
        {
          client_id: env.NEXT_PUBLIC_YANDEX_CLIENT_ID,
          response_type: "code",
          optional_scope: "login:avatar",
          redirect_uri: `${env.NEXT_PUBLIC_APP_URL}/oauth/yandex`,
        },
        "https://oauth.yandex.ru",
        {
          view: "button",
          parentId: "yandex-oauth",
          buttonSize: "xs",
          buttonView: "main",
          buttonTheme: resolvedTheme,
          buttonBorderRadius: "8",
          buttonIcon: "ya",
        },
      )
        .then(({ handler }) => handler())
        .then((data) => console.log("Сообщение с токеном", data))
        .catch((error) => console.log("Обработка ошибки", error));
    }

    const handleMessage = (
      event: MessageEvent<{ type: "AUTH_SUCCESS" | "AUTH_ERROR" }>,
    ) => {
      if (event.origin !== window.location.origin) return;

      switch (event.data.type) {
        case "AUTH_SUCCESS":
          router.push("/dashboard");
          break;
        case "AUTH_ERROR":
          toast.error("Ошибка авторизации");
          break;
        default:
          break;
      }
    };

    window.addEventListener("message", handleMessage);
    return () => window.removeEventListener("message", handleMessage);
  }, [resolvedTheme, router]);

  return <div id="yandex-oauth" />;
};
