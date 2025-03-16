"use client";

import { type TEmailVerificationSchema } from "~/utils/validation/email-verification";
import { EmailVerificationForm } from "~/components/forms/email-verification";
import { useRouter } from "next/navigation";
import { useMutation } from "@tanstack/react-query";
import { sendEmailVerification } from "~/api/auth";
import { toast } from "sonner";
import ProtectedRoute from "~/components/protected-route";
import type { AxiosError } from "axios";

export default function EmailVerificationPage() {
  const router = useRouter();

  const verifyEmail = useMutation({
    mutationFn: sendEmailVerification,
    onSuccess: () => {
      toast.success("Почта подтверждена");
      router.replace("/dashboard");
    },
    onError: (error: AxiosError<{ code: string; message: string }>) => {
      if (error.response?.data?.code === "") {
      }
    },
  });

  const onSubmit = async (data: TEmailVerificationSchema) => {
    await verifyEmail.mutateAsync(data);
  };

  return (
    <ProtectedRoute>
      <div className="grid gap-6">
        <h1 className="text-2xl font-bold">Подтвердите почту</h1>
        <EmailVerificationForm onSubmit={onSubmit} />
      </div>
    </ProtectedRoute>
  );
}
