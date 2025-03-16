"use client";

import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "~/components/ui/form";
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSlot,
} from "~/components/ui/input-otp";
import { REGEXP_ONLY_DIGITS } from "input-otp";
import { Button } from "~/components/ui/button";
import { useForm } from "react-hook-form";
import {
  emailVerificationSchema,
  type TEmailVerificationSchema,
} from "~/utils/validation/email-verification";
import { zodResolver } from "@hookform/resolvers/zod";
import React from "react";
import { useTimerStore } from "~/store/timer";
import { useCountdown } from "~/hooks/use-countdown";
import { SlidingNumber } from "~/components/ui/sliding-number";
import { useMutation } from "@tanstack/react-query";
import { logoutUser, requestEmailVerification } from "~/api/auth";
import { useAuthStore } from "~/store/auth";
import { toast } from "sonner";

type TEmailVerificationForm = {
  onSubmit: (data: TEmailVerificationSchema) => void;
};

const EmailVerificationForm = ({
  onSubmit,
}: React.PropsWithoutRef<TEmailVerificationForm>) => {
  const { startTimer } = useTimerStore();
  const { logout } = useAuthStore();
  const { formatedTime, isCooldown } = useCountdown();

  const form = useForm<TEmailVerificationSchema>({
    resolver: zodResolver(emailVerificationSchema),
    defaultValues: {
      otp: "",
    },
  });

  const requestOTP = useMutation({
    mutationFn: requestEmailVerification,
    onSuccess: async () => {
      startTimer(5.01);
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const onBackClicked = async () => {
    await logoutUser();
    logout();
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="flex flex-col gap-6"
      >
        <FormField
          control={form.control}
          name="otp"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Введите код подтверждения</FormLabel>
              <FormControl>
                <InputOTP maxLength={8} pattern={REGEXP_ONLY_DIGITS} {...field}>
                  <InputOTPGroup className="m-auto">
                    <InputOTPSlot index={0} />
                    <InputOTPSlot index={1} />
                    <InputOTPSlot index={2} />
                    <InputOTPSlot index={3} />
                    <InputOTPSlot index={4} />
                    <InputOTPSlot index={5} />
                    <InputOTPSlot index={6} />
                    <InputOTPSlot index={7} />
                  </InputOTPGroup>
                </InputOTP>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        {isCooldown ? (
          <div className="text-muted-foreground flex gap-1 text-sm text-nowrap">
            Запросить код повторно через:
            <div className="flex">
              <SlidingNumber value={formatedTime.minutes} />
              <span>:</span>
              <SlidingNumber value={formatedTime.seconds} padStart />
            </div>
          </div>
        ) : (
          <span
            onClick={async () => {
              await requestOTP.mutateAsync();
            }}
            className="text-muted-foreground hover:text-foreground w-fit cursor-pointer text-sm underline-offset-4 hover:underline"
          >
            Запросить код
          </span>
        )}

        <div className="grid gap-2">
          <Button type="submit">Подтвердить</Button>
          <Button variant="secondary" onClick={onBackClicked} type="button">
            Назад
          </Button>
        </div>
      </form>
    </Form>
  );
};

export { EmailVerificationForm };
