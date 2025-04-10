import Cropper, { type Area } from "react-easy-crop";
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
import { useCallback, useState } from "react";
import { getCroppedImg } from "~/lib/crop-images";
import { Button } from "~/components/ui/button";
import {
  FlipHorizontalIcon,
  FlipVerticalIcon,
  RotateCcwSquareIcon,
  RotateCwSquare,
} from "lucide-react";

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
  const [crop, setCrop] = useState({ x: 0, y: 0 });
  const [zoom, setZoom] = useState(1);
  const [rotation, setRotation] = useState(0);
  const [flip, setFlip] = useState({ horizontal: false, vertical: false });
  const [croppedAreaPixels, setCroppedAreaPixels] = useState<Area | null>(null);
  const isMobile = useIsMobile();

  const onCropComplete = useCallback((_: Area, croppedPixels: Area) => {
    setCroppedAreaPixels(croppedPixels);
  }, []);
  const handleSave = async () => {
    const cropped = await getCroppedImg(
      URL.createObjectURL(file),
      croppedAreaPixels!,
      rotation,
      flip,
    );
    onSave(cropped);
    onClose();
  };

  if (isMobile) {
    return (
      <Drawer open={open} onOpenChange={onClose} dismissible={false}>
        <DrawerContent>
          <DrawerHeader hidden>
            <DrawerTitle>Редактор изображения</DrawerTitle>
          </DrawerHeader>
          <div className="bg-muted relative m-4 aspect-square overflow-hidden rounded-lg">
            <Cropper
              image={file ? URL.createObjectURL(file) : ""}
              transform={[
                `translate(${crop.x}px, ${crop.y}px)`,
                `rotateZ(${rotation}deg)`,
                `rotateY(${flip.horizontal ? 180 : 0}deg)`,
                `rotateX(${flip.vertical ? 180 : 0}deg)`,
                `scale(${zoom})`,
              ].join(" ")}
              crop={crop}
              onCropChange={setCrop}
              zoom={zoom}
              onZoomChange={setZoom}
              rotation={rotation}
              onRotationChange={setRotation}
              aspect={1}
              objectFit="contain"
              onCropComplete={onCropComplete}
            />
          </div>
          <div className="mx-auto flex gap-4">
            <Button
              size="icon"
              variant="secondary"
              onClick={() =>
                setRotation((prev) => {
                  return prev - 90;
                })
              }
            >
              <RotateCcwSquareIcon />
            </Button>
            <Button
              size="icon"
              variant="secondary"
              onClick={() =>
                setFlip((prev) => {
                  return {
                    ...prev,
                    horizontal: !prev.horizontal,
                  };
                })
              }
            >
              <FlipHorizontalIcon />
            </Button>
            <Button
              size="icon"
              variant="secondary"
              onClick={() =>
                setFlip((prev) => {
                  return {
                    ...prev,
                    vertical: !prev.vertical,
                  };
                })
              }
            >
              <FlipVerticalIcon />
            </Button>
            <Button
              size="icon"
              variant="secondary"
              onClick={() =>
                setRotation((prev) => {
                  return prev + 90;
                })
              }
            >
              <RotateCwSquare />
            </Button>
          </div>
          <DrawerFooter>
            <Button size="sm" onClick={handleSave}>
              Сохранить
            </Button>
            <Button size="sm" variant="outline" onClick={onClose}>
              Отменить
            </Button>
          </DrawerFooter>
        </DrawerContent>
      </Drawer>
    );
  }

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent>
        <DialogHeader hidden>
          <DialogTitle>Редактор изображения</DialogTitle>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}
