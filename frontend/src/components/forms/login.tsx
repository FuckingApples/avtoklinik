"use client";

import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "~/components/ui/form";
import { useForm } from "react-hook-form";
import { signInSchema, type TSignInSchema } from "~/utils/validation/auth";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "~/components/ui/input";
import { Button } from "~/components/ui/button";
import { useLoginUser } from "~/hooks/use-user";
import Link from "next/link";
import { AlertCircle, LoaderCircle } from "lucide-react";
import { Alert, AlertDescription, AlertTitle } from "~/components/ui/alert";
import type { AxiosError } from "axios";
import { useQueryState } from "nuqs";

export const LoginForm = () => {
  const [redirect] = useQueryState("redirect");
  const form = useForm<TSignInSchema>({
    resolver: zodResolver(signInSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });
  const loginUser = useLoginUser(redirect, (error: AxiosError) => {
    if (error.response?.status === 401) {
      form.setError("root", { message: "Пароль или email указаны неверно" });
    }
  });

  const onSubmit = async (data: TSignInSchema) => {
    await loginUser.mutateAsync(data);
  };

  return (
    <Form {...form}>
      <form
        className="flex flex-col gap-6"
        onSubmit={form.handleSubmit(onSubmit)}
      >
        <div className="flex flex-col items-center gap-2 text-center">
          <h1 className="text-2xl font-bold">Войдите в свой аккаунт</h1>
          <p className="text-muted-foreground text-sm text-balance">
            Нет аккаунта?{" "}
            <Link
              href="/register"
              className="hover:text-primary underline underline-offset-4"
            >
              Зарегистрируйтесь
            </Link>
          </p>
        </div>
        {form.formState.errors.root && (
          <Alert variant="destructive">
            <AlertCircle className="size-4" />
            <AlertTitle>Ошибка</AlertTitle>
            <AlertDescription>
              {form.formState.errors.root.message}
            </AlertDescription>
          </Alert>
        )}
        <div className="grid gap-4">
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl>
                  <Input
                    autoComplete="work email"
                    type="email"
                    placeholder="example@yandex.ru"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <div className="flex items-center">
                  <FormLabel>Пароль</FormLabel>
                  <Link
                    href="/login/recovery"
                    className="ml-auto text-sm underline-offset-4 hover:underline"
                  >
                    Забыли пароль?
                  </Link>
                </div>
                <FormControl>
                  <Input
                    type="password"
                    autoComplete="new-password"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" disabled={loginUser.isPending}>
            {loginUser.isPending ? (
              <LoaderCircle className="animate-spin" />
            ) : (
              "Войти"
            )}
          </Button>
        </div>
      </form>
    </Form>
  );
};
