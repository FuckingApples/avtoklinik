import { z } from "zod";

export const emailVerificationSchema = z.object({
  otp: z.string().min(8, { message: "Код должен содержать 8 цифр" }),
});

export type TEmailVerificationSchema = z.infer<typeof emailVerificationSchema>;
