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
import { useCallback, useState } from "react";
import { ImageCropDialog } from "~/components/modals/image-crop";
import type { FileRejection } from "react-dropzone";
import { cn } from "~/lib/utils";

export default function DetailsTab({
  form,
}: {
  form: UseFormReturn<TUserSettingsSchema>;
}) {
  const [file, setFile] = useState<File | null>(null);
  const [open, setOpen] = useState(false);

  const updateUser = useUpdateUser((error: AxiosError<ErrorResponse>) => {
    if (error.response?.data.code === "user_does_not_exists") {
      form.setError("root", { message: "Пользователь не зарегистрирован" });
    } else {
      toast.error(error.message);
    }
  });

  const onDropAccepted = useCallback((acceptedFiles: File[]) => {
    setFile(acceptedFiles[0]!);
    setOpen(true);
  }, []);

  const onDropRejected = useCallback(
    (fileRejections: FileRejection[]) => {
      fileRejections.some(({ errors }) => {
        errors.some((err) => {
          if (err.code === "too-many-files") {
            form.setError("image", { message: "Слишком много файлов" });
          }
        });
      });
    },
    [form],
  );

  const onImageSave = (editedFile: File) => {
    form.setValue("image", editedFile, { shouldDirty: true });
  };

  const onSubmit = async (data: TUserSettingsSchema) => {
    await updateUser.mutateAsync(data);
    form.reset({
      first_name: data?.first_name,
      last_name: data?.last_name,
      email: data?.email,
    });
  };

  return (
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
            <FormItem className="md:flex">
              <div className="flex-1">
                <FormLabel>Имя</FormLabel>
                <FormDescription>Ваше имя</FormDescription>
              </div>
              <FormControl className="flex-1">
                <div>
                  <Input {...field} />
                  <FormMessage />
                </div>
              </FormControl>
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="last_name"
          render={({ field }) => (
            <FormItem className="md:flex">
              <div className="flex-1">
                <FormLabel>Фамилия</FormLabel>
                <FormDescription>Ваша фамилия</FormDescription>
              </div>
              <FormControl>
                <div className="flex-1">
                  <Input {...field} />
                  <FormMessage />
                </div>
              </FormControl>
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem className="md:flex">
              <div className="flex-1">
                <FormLabel>Почта</FormLabel>
                <FormDescription>Почта для входа и уведомлений</FormDescription>
              </div>
              <FormControl className="flex-1">
                <div>
                  <Input {...field} />
                  <FormMessage />
                </div>
              </FormControl>
            </FormItem>
          )}
        />
        <Separator />
        <FormItem className="md:flex">
          <div className="flex-1">
            <FormLabel
              className={cn(form.formState.errors?.image && "text-destructive")}
            >
              Фото профиля
            </FormLabel>
            <FormDescription>
              Фото увидят все в организациях, где вы состоите
            </FormDescription>
          </div>
          <div className="flex-1">
            <FormControl>
              <FileUpload
                options={{
                  maxFiles: 1,
                  maxSize: 5 * 1024 * 1024,
                  accept: {
                    "image/jpeg": [".jpeg", ".jpg"],
                    "image/png": [".png"],
                    "image/webp": [".webp"],
                  },
                  onDropAccepted,
                  onDropRejected,
                }}
              />
            </FormControl>
            <FormMessage>{form.formState.errors.image?.message}</FormMessage>
          </div>
        </FormItem>
        {file && (
          <ImageCropDialog
            onSave={onImageSave}
            file={file}
            open={open}
            onClose={() => setOpen(false)}
          />
        )}
      </form>
    </Form>
  );
}
