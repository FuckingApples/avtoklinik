"use client";

import { useEffect } from "react";
import axios from "axios";
import { env } from "~/env";

export default function CsrfTokenHandler() {
  useEffect(() => {
    const fetchCsrfToken = async () => {
      await axios
        .get(`${env.NEXT_PUBLIC_API_URL}/csrf_token`, { withCredentials: true })
        .then(() => {
          const csrfCookie = document.cookie
            .split("; ")
            .find((row) => row.startsWith("csrftoken="))
            ?.split("=")[1];

          if (!csrfCookie) {
            return Promise.reject(new Error("CSRF token not found"));
          }
        })
        .catch((error) => console.error("CSRF token fetch error", error));
    };

    void fetchCsrfToken();
  }, []);

  return null;
}
