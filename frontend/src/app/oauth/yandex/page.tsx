"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { yandexOAuth } from "~/api/auth";
import { useAuthStore } from "~/store/auth";
import { useQueryState } from "nuqs";

export default function YandexOAuthPage() {
  const { setAccessToken } = useAuthStore();
  const [code] = useQueryState("code");
  const router = useRouter();

  useEffect(() => {
    if (!code) {
      router.back();
    }

    const handleAuth = async () => {
      await yandexOAuth(code!)
        .then((data) => {
          setAccessToken(data.access);
          if (window.opener) {
            // eslint-disable-next-line @typescript-eslint/no-unsafe-call,@typescript-eslint/no-unsafe-member-access
            window.opener.postMessage(
              { type: "AUTH_SUCCESS", data },
              window.location.origin,
            );
            window.close();
          } else {
            router.push("/dashboard");
          }
        })
        .catch(() => {
          // eslint-disable-next-line @typescript-eslint/no-unsafe-call,@typescript-eslint/no-unsafe-member-access
          window.opener?.postMessage(
            { type: "AUTH_ERROR" },
            window.location.origin,
          );
        });
    };

    void handleAuth();
  }, [router, code, setAccessToken]);

  return <div>Авторизация...</div>;
}
