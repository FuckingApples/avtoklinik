import { useMutation, useQuery } from "@tanstack/react-query";
import { useUserStore } from "~/store/user";
import { createUser, getUserInfo } from "~/api/user";
import { loginUser } from "~/api/auth";
import { useAuthStore } from "~/store/auth";
import { useRouter } from "next/navigation";
import type { AxiosError } from "axios";
import type { LoginResponse } from "~/types/api";

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

export const useCreateUser = (onError: (error: AxiosError<never>) => void) => {
  const { setAccessToken } = useAuthStore();
  const router = useRouter();

  return useMutation({
    mutationFn: createUser,
    onSuccess: async (_, variables) => {
      const token = await loginUser({
        email: variables.email,
        password: variables.password,
      });
      setAccessToken(token.access);
      router.push("/register/verify");
    },
    onError,
  });
};

export const useLoginUser = (
  redirect: string | null,
  onError: (error: AxiosError<never>) => void,
) => {
  const { setAccessToken } = useAuthStore();
  const router = useRouter();

  return useMutation({
    mutationFn: loginUser,
    onSuccess: (data: LoginResponse) => {
      setAccessToken(data.access);
      if (data.is_email_verified) {
        if (redirect) {
          router.push(redirect);
        } else {
          router.push("/dashboard");
        }
      } else {
        router.push("/register/verify");
      }
    },
    onError,
  });
};
