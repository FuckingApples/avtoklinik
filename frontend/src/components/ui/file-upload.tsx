import { type DropzoneOptions, useDropzone } from "react-dropzone";
import { Input } from "~/components/ui/input";
import { UploadCloud } from "lucide-react";
import type { ControllerRenderProps, FieldValues } from "react-hook-form";
import { cn } from "~/lib/utils";

type FileUploadProps<T extends FieldValues> = {
  options?: DropzoneOptions;
  field: ControllerRenderProps<T>;
};

export default function FileUpload<T extends FieldValues>({
  options,
  field: { onChange },
}: FileUploadProps<T>) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone(options);

  return (
    <section>
      <label
        className={cn(
          "border-border hover:bg-primary-foreground relative flex w-full cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed py-6",
          isDragActive && "border-primary",
        )}
        {...getRootProps()}
      >
        <div
          className={cn(
            "text-muted-foreground text-center",
            isDragActive && "text-primary",
          )}
        >
          <UploadCloud className="mx-auto size-10" />
          <p className="mt-2 text-sm">Перетащите файлы для загрузки</p>
          <p className="text-xs">или нажмите, чтобы выбрать файлы</p>
        </div>
      </label>
      <Input
        type="file"
        className="hidden"
        {...getInputProps({
          onChange: (event) => onChange(event.target.files?.[0]),
        })}
      />
    </section>
  );
}
