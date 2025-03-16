"use client";

import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormDescription,
  FormMessage,
} from "~/components/ui/form";
import { Input } from "~/components/ui/input";
import { type UseFormReturn } from "react-hook-form";
import { Separator } from "~/components/ui/separator";
import type { TUserSettingsSchema } from "~/utils/validation/user-settings";
import FileUpload from "~/components/ui/file-upload";
import { useUpdateUser } from "~/hooks/use-user";
import { toast } from "sonner";
import type { AxiosError } from "axios";
import type { ErrorResponse } from "~/types/api";

export default function DetailsTab({
  form,
}: {
  form: UseFormReturn<TUserSettingsSchema>;
}) {
  const updateUser = useUpdateUser((error: AxiosError<ErrorResponse>) => {
    if (error.response?.data.code === "user_does_not_exists") {
      form.setError("root", { message: "Пользователь не зарегистрирован" });
    } else {
      toast.error(error.message);
    }
  });

  const onSubmit = async (data: TUserSettingsSchema) => {
    await updateUser.mutateAsync(data);
  };

  return (
    <section className="mx-3">
      <Form {...form}>
        <form
          id="user-settings"
          className="mb-3 flex flex-col gap-4"
          onSubmit={form.handleSubmit(onSubmit)}
        >
          <FormField
            control={form.control}
            name="first_name"
            render={({ field }) => (
              <FormItem>
                <div>
                  <FormLabel>Имя</FormLabel>
                  <FormDescription>Ваше имя</FormDescription>
                </div>
                <FormControl>
                  <Input {...field} />
                </FormControl>
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="last_name"
            render={({ field }) => (
              <FormItem>
                <div>
                  <FormLabel>Фамилия</FormLabel>
                  <FormDescription>Ваша фамилия</FormDescription>
                </div>
                <FormControl>
                  <Input {...field} />
                </FormControl>
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <div>
                  <FormLabel>Почта</FormLabel>
                  <FormDescription>
                    Почта для входа и уведомлений
                  </FormDescription>
                </div>
                <FormControl>
                  <Input {...field} />
                </FormControl>
              </FormItem>
            )}
          />
          <Separator />
          <FormField
            control={form.control}
            name="image"
            render={({ field }) => (
              <FormItem>
                <div>
                  <FormLabel>Фото профиля</FormLabel>
                  <FormDescription>
                    Фото увидят все в организациях, где вы состоите
                  </FormDescription>
                </div>
                <FormControl>
                  <FileUpload
                    field={field}
                    options={{
                      maxFiles: 1,
                      maxSize: 5 * 1024 * 1024,
                      accept: {
                        "image/jpeg": [".jpeg", ".jpg"],
                        "image/png": [".png"],
                        "image/webp": [".webp"],
                      },
                    }}
                  />
                </FormControl>
                <FormMessage></FormMessage>
              </FormItem>
            )}
          />
        </form>
      </Form>
    </section>
  );
}
