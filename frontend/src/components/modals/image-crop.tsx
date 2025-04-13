import {
  FixedCropper,
  ImageRestriction,
  Cropper,
  CropperPreview,
  type FixedCropperRef,
  type StencilSize,
  type CropperRef,
  type CropperPreviewRef,
} from "react-advanced-cropper";
import { useIsMobile } from "~/hooks/use-mobile";
import {
  Drawer,
  DrawerContent,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
} from "~/components/ui/drawer";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "~/components/ui/dialog";
import { Button } from "~/components/ui/button";
import {
  FlipHorizontalIcon,
  FlipVerticalIcon,
  RotateCcwSquareIcon,
  RotateCwSquare,
} from "lucide-react";
import { useRef } from "react";

import "react-advanced-cropper/dist/style.css";

type ImageCropProps = {
  file: File;
  open?: boolean;
  onClose: () => void;
  onSave: (file: File) => void;
};

export function ImageCropDialog({
  file,
  open = false,
  onClose,
  onSave,
}: ImageCropProps) {
  const cropperRef = useRef<FixedCropperRef>(null);
  const previewBigRef = useRef<CropperPreviewRef>(null);
  const previewSmallRef = useRef<CropperPreviewRef>(null);
  const isMobile = useIsMobile();

  const handleSave = () => {
    const ref = cropperRef.current;
    if (ref) {
      ref.getCanvas()?.toBlob((blob) => {
        if (blob) {
          onSave(new File([blob], "edited-image.jpg", { type: "image/webp" }));
        }
      }, "image/webp");
      onClose();
    }
  };

  const onUpdate = (cropper: CropperRef) => {
    previewBigRef.current?.update(cropper);
    previewSmallRef.current?.update(cropper);
  };

  const stencilSize: StencilSize = ({ boundary }) => {
    return {
      width: boundary.width - 80,
      height: boundary.width - 80,
    };
  };

  const rotate = (angle: number) => {
    const ref = cropperRef.current;

    if (ref) {
      ref.rotateImage(angle);
    }
  };

  const flip = (horizontal = false, vertical = false) => {
    const ref = cropperRef.current;

    if (ref) {
      ref.flipImage(horizontal, vertical);
    }
  };

  if (isMobile) {
    return (
      <Drawer open={open} onOpenChange={onClose} dismissible={false}>
        <DrawerContent>
          <DrawerHeader hidden>
            <DrawerTitle>Редактор изображения</DrawerTitle>
          </DrawerHeader>
          <FixedCropper
            ref={cropperRef}
            className="bg-muted! relative m-4 aspect-square rounded-lg"
            src={file ? URL.createObjectURL(file) : ""}
            stencilProps={{
              aspectRatio: 1,
              movable: false,
              resizable: false,
              lines: false,
              handlers: false,
            }}
            stencilSize={stencilSize}
            transformImage={{ adjustStencil: false }}
            imageRestriction={ImageRestriction.stencil}
          />
          <div className="mx-auto flex gap-4">
            <Button size="icon" variant="secondary" onClick={() => rotate(-90)}>
              <RotateCcwSquareIcon />
            </Button>
            <Button size="icon" variant="secondary" onClick={() => flip(true)}>
              <FlipHorizontalIcon />
            </Button>
            <Button
              size="icon"
              variant="secondary"
              onClick={() => flip(false, true)}
            >
              <FlipVerticalIcon />
            </Button>
            <Button size="icon" variant="secondary" onClick={() => rotate(90)}>
              <RotateCwSquare />
            </Button>
          </div>
          <DrawerFooter>
            <Button size="lg" onClick={handleSave}>
              Сохранить
            </Button>
            <Button size="lg" variant="outline" onClick={onClose}>
              Отменить
            </Button>
          </DrawerFooter>
        </DrawerContent>
      </Drawer>
    );
  }

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="flex flex-row gap-5">
        <DialogHeader hidden>
          <DialogTitle>Редактор изображения</DialogTitle>
        </DialogHeader>
        <Cropper
          ref={cropperRef}
          className="bg-muted! relative aspect-square flex-2 rounded-lg"
          src={file ? URL.createObjectURL(file) : ""}
          stencilProps={{
            aspectRatio: 1,
          }}
          transformImage={{ adjustStencil: false }}
          imageRestriction={ImageRestriction.fillArea}
          onUpdate={onUpdate}
        />
        <div className="flex flex-1 flex-col justify-between gap-3">
          <div>
            <h6 className="text-foreground mb-1 text-lg font-semibold">
              Предпросмотр
            </h6>
            <div className="flex justify-between">
              <CropperPreview
                ref={previewBigRef}
                className="size-25 rounded-xl"
              />
              <CropperPreview
                ref={previewSmallRef}
                className="size-14 rounded-lg"
              />
            </div>
          </div>
          <div className="mx-auto flex gap-2">
            <Button size="icon" variant="secondary" onClick={() => rotate(-90)}>
              <RotateCcwSquareIcon />
            </Button>
            <Button size="icon" variant="secondary" onClick={() => flip(true)}>
              <FlipHorizontalIcon />
            </Button>
            <Button
              size="icon"
              variant="secondary"
              onClick={() => flip(false, true)}
            >
              <FlipVerticalIcon />
            </Button>
            <Button size="icon" variant="secondary" onClick={() => rotate(90)}>
              <RotateCwSquare />
            </Button>
          </div>
          <div className="flex flex-col gap-2">
            <Button size="sm" onClick={handleSave}>
              Сохранить
            </Button>
            <Button size="sm" variant="outline" onClick={onClose}>
              Отменить
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
}
