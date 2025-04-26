"use client";

import { useState, useEffect } from "react";
import { Check, X } from "lucide-react";
import { CarTableSettings } from "~/types/car";
import { 
  Dialog, 
  DialogContent, 
  DialogHeader, 
  DialogTitle, 
  DialogFooter
} from "~/components/ui/dialog";
import { Button } from "~/components/ui/button";
import { Label } from "~/components/ui/label";
import { Separator } from "~/components/ui/separator";
import { ScrollArea } from "~/components/ui/scroll-area";

interface CarTableSettingsProps {
  open: boolean;
  onClose: () => void;
  settings: CarTableSettings;
  onSave: (settings: CarTableSettings) => void;
}

export function CarTableSettingsDialog({ 
  open, 
  onClose, 
  settings, 
  onSave 
}: CarTableSettingsProps) {
  const [localSettings, setLocalSettings] = useState<CarTableSettings>(settings);

  useEffect(() => {
    if (open) {
      setLocalSettings(settings);
    }
  }, [open, settings]);
  
  const handleToggleColumn = (columnKey: string) => {
    if (columnKey === 'actions') return;
    
    setLocalSettings(prev => ({
      ...prev,
      columns: prev.columns.map(col => 
        col.key === columnKey ? { ...col, visible: !col.visible } : col
      )
    }));
  };
  
  const handleSave = () => {
    onSave(localSettings);
    onClose();
  };
  
  return (
    <Dialog open={open} onOpenChange={(isOpen) => !isOpen && onClose()}>
      <DialogContent className="sm:max-w-[450px]">
        <DialogHeader>
          <DialogTitle>Настройки отображения таблицы</DialogTitle>
        </DialogHeader>
        
        <Separator className="my-4" />
        
        <ScrollArea className="h-[350px] pr-4">
          <div className="space-y-6">
            <div className="space-y-4">
              <h3 className="font-semibold">Количество записей на странице</h3>
              <div className="space-y-3">
                <div className="flex items-center">
                  <div className="relative w-full px-1">
                    <select
                      className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                      value={localSettings.pageSize}
                      onChange={(e) => setLocalSettings(prev => ({
                        ...prev,
                        pageSize: parseInt(e.target.value)
                      }))}
                    >
                      <option value="5">5 записей</option>
                      <option value="10">10 записей</option>
                      <option value="20">20 записей</option>
                      <option value="50">50 записей</option>
                      <option value="100">100 записей</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="space-y-4">
              <h3 className="font-semibold">Видимые колонки</h3>
              <div className="space-y-3">
                {localSettings.columns.map((column) => (
                  <div 
                    key={column.key} 
                    className={`flex items-center justify-between p-2 rounded-md hover:bg-muted cursor-pointer ${column.key === 'actions' ? 'opacity-70' : ''}`}
                    onClick={() => handleToggleColumn(column.key)}
                  >
                    <div className="flex items-center gap-2">
                      <div 
                        className={`flex items-center justify-center size-6 rounded-md border ${column.visible ? 'bg-primary border-primary text-primary-foreground dark:text-black' : 'border-input'}`}
                      >
                        {column.visible && <Check className="h-4 w-4" />}
                      </div>
                      <Label htmlFor={`column-${column.key}`} className="cursor-pointer">
                        {column.title}
                      </Label>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </ScrollArea>
        
        <DialogFooter className="mt-4">
          <Button variant="outline" onClick={onClose} className="inline-flex items-center">
            <span className="flex items-center pr-2">
              <X className="size-4 mr-1.5" />
              Отмена
            </span>
          </Button>
          <Button onClick={handleSave} className="inline-flex items-center">
            <span className="flex items-center pr-2">
              <Check className="size-4 mr-1.5" />
              Сохранить
            </span>
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
} 