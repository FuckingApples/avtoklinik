"use client";

import React from "react";
import { Car } from "~/types/car";
import { Button } from "~/components/ui/button";
import { Trash } from "lucide-react";
import { 
  Dialog, 
  DialogContent, 
  DialogHeader, 
  DialogTitle, 
  DialogFooter 
} from "~/components/ui/dialog";

interface DeleteCarDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onConfirm: () => void;
  car: Car | null | undefined;
}

export function DeleteCar({ open, onOpenChange, onConfirm, car }: DeleteCarDialogProps) {
  const handleConfirm = () => {
    onConfirm();
    onOpenChange(false);
  };

  return (
    <Dialog open={open} onOpenChange={(isOpen) => !isOpen && onOpenChange(false)}>
      <DialogContent className="sm:max-w-[450px]">
        <DialogHeader>
          <DialogTitle>Удаление автомобиля</DialogTitle>
        </DialogHeader>
        
        <div>
          <p className="text-muted-foreground text-sm">
            {car ? 
              `Вы уверены, что хотите удалить автомобиль ${car.brand} ${car.model} (${car.year})?` :
              'Вы уверены, что хотите удалить этот автомобиль?'
            }
            {' '}Это действие невозможно отменить.
          </p>
        </div>
        
        <DialogFooter className="pt-2">
          <div className="flex w-full justify-start gap-3">
            <Button 
              variant="outline" 
              onClick={() => onOpenChange(false)}
              className="min-w-32 bg-black text-white hover:bg-black/80 hover:text-white"
            >
              Отменить
            </Button>
            <Button 
              variant="outline"
              onClick={handleConfirm}
              className="text-destructive hover:text-destructive hover:bg-destructive/10 min-w-24"
            >
              <Trash className="mr-2 h-4 w-4" />
              Удалить
            </Button>
          </div>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
} 