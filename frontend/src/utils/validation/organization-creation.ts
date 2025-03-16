import { z } from "zod";

export const organizationCreationSchema = z.object({
  name: z
    .string({ message: "Поле обязательно" })
    .min(3, { message: "Имя должно содержать минимум 3 символа" }),
});

export type TOrganizationCreationSchema = z.infer<
  typeof organizationCreationSchema
>;
