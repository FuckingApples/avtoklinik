import { type DropzoneOptions, useDropzone } from "react-dropzone";
import { Input } from "~/components/ui/input";
import { UploadCloud } from "lucide-react";
import { cn } from "~/lib/utils";
import type { ChangeEvent } from "react";

type FileUploadProps = {
  options?: DropzoneOptions;
  onChange: (event: ChangeEvent<HTMLInputElement>) => unknown;
};

export default function FileUpload({ options, onChange }: FileUploadProps) {
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
        {...getInputProps({
          onChange,
        })}
      />
    </section>
  );
}
