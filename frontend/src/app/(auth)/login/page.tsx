"use client";

import { Input } from "~/components/ui/input";
import { Label } from "~/components/ui/label";
import Link from "next/link";
import { Button } from "~/components/ui/button";
import { useForm } from "react-hook-form";
import { signInSchema, type TSignInSchema } from "~/utils/validation/auth";
import { zodResolver } from "@hookform/resolvers/zod";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuthStore } from "~/store/auth";
import { useMutation } from "@tanstack/react-query";
import { type LoginResponse, loginUser } from "~/api/auth";
import type { AxiosError } from "axios";
import { Alert, AlertDescription, AlertTitle } from "~/components/ui/alert";
import { AlertCircle } from "lucide-react";

export default function LoginPage() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<TSignInSchema>({ resolver: zodResolver(signInSchema) });

  const setAccessToken = useAuthStore((state) => state.setAccessToken);

  const mutation = useMutation({
    mutationFn: loginUser,
    onSuccess: (data: LoginResponse) => {
      setAccessToken(data.access);
      if (data.is_email_verified) {
        const redirect = searchParams.get("redirect");
        if (redirect) {
          router.push(redirect);
        } else {
          router.push("/dashboard");
        }
      } else {
        router.push("/register/verify");
      }
    },
    onError: (error: AxiosError) => {
      if (error.response?.status === 401) {
        setError("root", { message: "Пароль или email указаны неверно" });
      }
    },
  });

  const onSubmit = async (data: TSignInSchema) => {
    await mutation.mutateAsync(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">
      <div className="flex flex-col items-center gap-2 text-center">
        <h1 className="text-2xl font-bold">Войдите в свой аккаунт</h1>
        <p className="text-muted-foreground text-sm text-balance">
          Введите свой email, чтобы войти в аккаунт
        </p>
      </div>
      {errors.root && (
        <Alert variant="destructive">
          <AlertCircle className="size-4" />
          <AlertTitle>Ошибка</AlertTitle>
          <AlertDescription>{errors.root.message}</AlertDescription>
        </Alert>
      )}
      <div className="grid gap-6">
        <div className="grid gap-2">
          <Label htmlFor="email">Email</Label>
          <Input
            id="email"
            type="email"
            placeholder="example@yandex.ru"
            className={errors.email ? "border-red-600" : ""}
            {...register("email")}
          />
          {errors.email && (
            <p className="validation-error">{errors.email.message}</p>
          )}
        </div>
        <div className="grid gap-2">
          <div className="flex items-center">
            <Label htmlFor="password">Пароль</Label>
            <Link
              href="/password/reset"
              className="ml-auto text-sm underline-offset-4 hover:underline"
            >
              Забыли пароль?
            </Link>
          </div>
          <Input
            id="password"
            type="password"
            className={errors.password ? "border-red-600" : ""}
            {...register("password")}
          />
          {errors.password && (
            <p className="validation-error">{errors.password.message}</p>
          )}
        </div>
        <Button type="submit" className="w-full">
          Войти
        </Button>
        {/*<div className="after:border-border relative text-center text-sm after:absolute after:inset-0 after:top-1/2 after:z-0 after:flex after:items-center after:border-t">*/}
        {/*  <span className="bg-background text-muted-foreground relative z-10 px-2">*/}
        {/*    или*/}
        {/*  </span>*/}
        {/*</div>*/}
      </div>
      <div className="text-center text-sm">
        Нет аккаунта?{" "}
        <Link href="register" className="underline underline-offset-4">
          Зарегистрируйтесь
        </Link>
      </div>
    </form>
  );
}
