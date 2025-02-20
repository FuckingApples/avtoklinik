"use client";

import React, { useState } from "react";
import {
  QueryClient,
  QueryClientProvider,
  MutationCache,
} from "@tanstack/react-query";
import { toast } from "sonner";

export default function ReactQueryProvider({
  children,
}: React.PropsWithChildren) {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        mutationCache: new MutationCache({
          onError: (error) => {
            toast.error(error.message, {});
          },
        }),
      }),
  );
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}
