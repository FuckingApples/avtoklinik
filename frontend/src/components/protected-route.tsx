"use client";

import type React from "react";
import { useEffect, useState } from "react";
import { useAuthStore } from "~/store/auth";
import { useRouter } from "next/navigation";
import { LoaderCircle } from "lucide-react";

export default function ProtectedRoute({ children }: React.PropsWithChildren) {
  const { accessToken } = useAuthStore();
  const router = useRouter();
  const [isHydrated, setIsHydrated] = useState(false);

  useEffect(() => {
    const unsubscribe = useAuthStore.persist.onFinishHydration(() => {
      setIsHydrated(true);
    });
    if (useAuthStore.persist.hasHydrated()) {
      setIsHydrated(true);
    }

    return unsubscribe;
  }, []);

  useEffect(() => {
    if (!isHydrated) return;

    if (!accessToken) {
      router.push("/login");
    }
  }, [accessToken, router, isHydrated]);

  if (!isHydrated || !accessToken)
    return (
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
        <LoaderCircle className="text-muted-foreground size-10 animate-spin" />
      </div>
    );

  return children;
}
