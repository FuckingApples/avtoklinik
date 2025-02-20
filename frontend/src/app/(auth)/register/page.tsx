"use client";

import { Label } from "~/components/ui/label";
import { Input } from "~/components/ui/input";
import { Button } from "~/components/ui/button";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { signUpSchema, type TSignUpSchema } from "~/utils/validation/auth";
import { useMutation } from "@tanstack/react-query";
import { LoaderCircle } from "lucide-react";
import { useAuthStore } from "~/store/auth";
import { loginUser, registerUser } from "~/api/auth";

export default function RegisterPage() {
  const router = useRouter();
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors },
  } = useForm<TSignUpSchema>({ resolver: zodResolver(signUpSchema) });
  const setAccessToken = useAuthStore((state) => state.setAccessToken);

  const mutation = useMutation({
    mutationFn: registerUser,
    onSuccess: async (_, variables: TSignUpSchema) => {
      try {
        const token = await loginUser({
          email: variables.email,
          password: variables.password,
        });
        setAccessToken(token.access);
        router.push("/dashboard");
      } catch {
        setError("root", { message: "Ошибка при входе" });
      }
    },
    onError: (error: Error) => {
      setError("root", { message: error.message });
      return Promise.reject(error);
    },
  });

  const onSubmit = async (data: TSignUpSchema): Promise<void> => {
    await mutation.mutateAsync(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="flex flex-col gap-6">
      {errors.root && errors.root.message}
      <div className="flex flex-col items-center gap-2 text-center">
        <h1 className="text-2xl font-bold">Создайте новый аккаунт</h1>
        <p className="text-balance text-sm text-muted-foreground">
          Введите свои данные, чтобы создать аккаунт
        </p>
      </div>
      <div className="grid gap-6">
        <div className="grid gap-6">
          <div className="grid grid-cols-2 gap-2">
            <div className="grid gap-2">
              <Label htmlFor="last_name">Фамилия</Label>
              <Input
                id="last_name"
                type="text"
                className={errors.last_name ? "border-red-600" : ""}
                {...register("last_name")}
              />
            </div>
            <div className="grid gap-2">
              <Label htmlFor="first_name">Имя</Label>
              <Input
                id="first_name"
                type="text"
                className={errors.first_name ? "border-red-600" : ""}
                {...register("first_name")}
              />
            </div>
            <div className="col-span-2">
              {errors.last_name && (
                <p className="validation-error">{errors.last_name.message}</p>
              )}
              {errors.first_name && (
                <p className="validation-error">{errors.first_name.message}</p>
              )}
            </div>
          </div>
        </div>
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
          <Label htmlFor="password">Пароль</Label>
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
        <div className="grid gap-2">
          <Label htmlFor="re_password">Повторите пароль</Label>
          <Input
            id="re_password"
            type="password"
            className={errors.re_password ? "border-red-600" : ""}
            {...register("re_password")}
          />
          {errors.re_password && (
            <p className="validation-error">{errors.re_password.message}</p>
          )}
        </div>
        <div className="grid gap-2">
          <Button
            type="submit"
            className="w-full"
            disabled={mutation.isPending}
          >
            {mutation.isPending ? (
              <LoaderCircle className="animate-spin" />
            ) : (
              "Продолжить"
            )}
          </Button>
          <div className="text-balance text-center text-xs text-muted-foreground [&_a]:underline [&_a]:underline-offset-4 hover:[&_a]:text-primary">
            Нажимая «Продолжить», вы принимаете{" "}
            <Link href="terms">пользовательское соглашение</Link> и{" "}
            <Link href="privacy">политику конфиденциальности</Link>
          </div>
        </div>
        {/*<div className="after:border-border relative text-center text-sm after:absolute after:inset-0 after:top-1/2 after:z-0 after:flex after:items-center after:border-t">*/}
        {/*  <span className="bg-background text-muted-foreground relative z-10 px-2">*/}
        {/*    или*/}
        {/*  </span>*/}
        {/*</div>*/}
      </div>
      <div className="text-center text-sm">
        Уже зарегистрированы?{" "}
        <Link href="login" className="underline underline-offset-4">
          Войдите
        </Link>
      </div>
    </form>
  );
}
