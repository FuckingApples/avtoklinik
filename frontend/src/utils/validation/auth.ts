import { z } from "zod";

export const signUpSchema = z
  .object({
    first_name: z.string().min(1, { message: "Имя обязательно" }),
    last_name: z.string().min(1, { message: "Фамилия обязательна" }),
    email: z.string().email({ message: "Неверный email" }),
    password: z
      .string()
      .min(8, { message: "Пароль должен быть от 8 символов" }),
    re_password: z.string(),
  })
  .refine((data) => data.password === data.re_password, {
    message: "Пароли должны соответсвовать",
    path: ["re_password"],
  });

export type TSignUpSchema = z.infer<typeof signUpSchema>;

export const signInSchema = z.object({
  email: z.string().email({ message: "Неверный email" }),
  password: z.string().min(8, { message: "Пароль должен быть от 8 символов" }),
});

export type TSignInSchema = z.infer<typeof signInSchema>;
