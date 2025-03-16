import { z } from "zod";

const MAX_FILE_SIZE = 5 * 1024 * 1024;

const ACCEPTED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"];

export const userSettingsSchema = z.object({
  first_name: z.string(),
  last_name: z.string(),
  email: z.string().email(),
  image: z
    .instanceof(File)
    .optional()
    .refine(
      (file) => (file ? ACCEPTED_IMAGE_TYPES.includes(file.type) : true),
      "Неподдерживаемый формат. Можно загрузить только .jpeg, .jpg, .webp и .png",
    )
    .refine(
      (file) => (file ? file.size <= MAX_FILE_SIZE : true),
      "Максимальный размер файла: 5МБ",
    ),
});

export type TUserSettingsSchema = z.infer<typeof userSettingsSchema>;
