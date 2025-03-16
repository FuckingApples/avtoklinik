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
import { signUpSchema, type TSignUpSchema } from "~/utils/validation/auth";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "~/components/ui/input";
import { Button } from "~/components/ui/button";
import { useCreateUser } from "~/hooks/use-user";
import Link from "next/link";
import { AlertCircle, LoaderCircle } from "lucide-react";
import { Alert, AlertDescription, AlertTitle } from "~/components/ui/alert";
import type { AxiosError } from "axios";
import type { ErrorResponse } from "~/types/api";
import { toast } from "sonner";

export const RegistrationForm = () => {
  const form = useForm<TSignUpSchema>({
    resolver: zodResolver(signUpSchema),
    defaultValues: {
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      re_password: "",
    },
  });
  const createUser = useCreateUser((error: AxiosError<ErrorResponse>) => {
    if (error.response?.data.code === "user_already_exists") {
      form.setError("root", { message: "Пользователь уже зарегистрирован" });
    } else {
      toast.error(error.message);
    }
  });

  const onSubmit = async (data: TSignUpSchema) => {
    await createUser.mutateAsync(data);
  };

  return (
    <Form {...form}>
      <form
        className="flex flex-col gap-6"
        onSubmit={form.handleSubmit(onSubmit)}
      >
        <div className="flex flex-col items-center gap-2 text-center">
          <h1 className="text-2xl font-bold">Создайте новый аккаунт</h1>
          <p className="text-muted-foreground text-sm text-balance">
            Уже зарегистрированы?{" "}
            <Link
              href="login"
              className="hover:text-primary underline underline-offset-4"
            >
              Войдите
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
          <div className="grid grid-cols-2 items-start gap-2">
            <FormField
              control={form.control}
              name="first_name"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Имя</FormLabel>
                  <FormControl>
                    <Input autoComplete="given-name" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="last_name"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Фамилия</FormLabel>
                  <FormControl>
                    <Input autoComplete="family-name" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>
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
                <FormLabel>Пароль</FormLabel>
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
          <FormField
            control={form.control}
            name="re_password"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Повторите пароль</FormLabel>
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
          <div className="grid gap-2">
            <Button type="submit" disabled={createUser.isPending}>
              {createUser.isPending ? (
                <LoaderCircle className="animate-spin" />
              ) : (
                "Продолжить"
              )}
            </Button>
            <div className="text-muted-foreground [&_a]:hover:text-primary text-center text-xs text-balance [&_a]:underline [&_a]:underline-offset-4">
              Нажимая «Продолжить», вы принимаете{" "}
              <Link href="/leagal/terms">пользовательское соглашение</Link> и{" "}
              <Link href="/leagal/privacy">политику конфиденциальности</Link>
            </div>
          </div>
        </div>
      </form>
    </Form>
  );
};
