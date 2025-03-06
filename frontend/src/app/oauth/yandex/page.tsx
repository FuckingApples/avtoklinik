"use client";

import { useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { yandexOAuth } from "~/api/auth";
import { useAuthStore } from "~/store/auth";
import type { AxiosError } from "axios";
import type { ErrorResponse } from "~/types/api";

export default function YandexOAuthPage() {
  const { setAccessToken } = useAuthStore();
  const searchParams = useSearchParams();
  const router = useRouter();

  useEffect(() => {
    const code = searchParams.get("code");
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
        .catch((error: AxiosError<ErrorResponse>) => {
          // eslint-disable-next-line @typescript-eslint/no-unsafe-call,@typescript-eslint/no-unsafe-member-access
          window.opener?.postMessage(
            { type: "AUTH_ERROR", error },
            window.location.origin,
          );
        });
    };

    void handleAuth();
  }, [router, searchParams, setAccessToken]);

  return <div>Авторизация...</div>;
}
