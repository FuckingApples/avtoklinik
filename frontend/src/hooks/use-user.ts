"use client";

import { useQuery } from "@tanstack/react-query";
import { useUserStore } from "~/store/user";
import { getUserInfo } from "~/api/user";

export const useUser = () => {
  const { setUser } = useUserStore();

  return useQuery({
    queryKey: ["user"],
    queryFn: async () => {
      const data = await getUserInfo();
      setUser(data);
      return data;
    },
    staleTime: 1000 * 60 * 5, // Кэш 5 минут
  });
};
