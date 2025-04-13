"use client";

import { useState, useMemo, useEffect } from "react";
import { Edit, Trash } from "lucide-react";
import { Car } from "~/types/car";
import { 
  Sheet, 
  SheetContent, 
  SheetHeader, 
  SheetTitle, 
  SheetFooter 
} from "~/components/ui/sheet";
import { Button } from "~/components/ui/button";
import { Separator } from "~/components/ui/separator";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "~/components/ui/tabs";
import { ScrollArea } from "~/components/ui/scroll-area";
import { getCountryName } from "~/api/registries";
import { DeleteCar } from "~/components/modals/delete-car";

interface CarDetailProps {
  car: Car | null;
  open: boolean;
  onClose: () => void;
  orgId: string;
  onEdit?: (car: Car) => void;
  onDelete?: (carId: string) => void;
}

export function CarDetails({ car, open, onClose, onEdit, onDelete }: CarDetailProps) {
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [isSheetOpen, setIsSheetOpen] = useState(false);

  useEffect(() => {
    if (open) {
      setIsSheetOpen(true);
    }
  }, [open]);
  
  const countryName = useMemo(() => {
    if (!car?.license_plate_region) return "Неизвестно";
    return getCountryName(car.license_plate_region);
  }, [car?.license_plate_region]);

  const handleDelete = () => {
    if (car && onDelete) {
      onDelete(car.id);
    }
    setDeleteDialogOpen(false);
  };

  const handleSheetOpenChange = (open: boolean) => {
    setIsSheetOpen(open);
    
    if (!open) {
      setTimeout(() => {
        onClose();
      }, 300);
    }
  };

  if (!car) return null;

  return (
    <>
      <Sheet open={isSheetOpen} onOpenChange={handleSheetOpenChange}>
        <SheetContent
          side="right"
          className="w-[450px] max-w-full p-0 sm:max-w-[450px]"
        >
          <SheetHeader className="border-b p-6">
            <div className="flex items-center justify-between">
              <SheetTitle className="text-xl">
                Информация об автомобиле
              </SheetTitle>
            </div>
          </SheetHeader>

          <ScrollArea className="h-[calc(100vh-12rem)]">
            <div className="px-6 py-4">
              <Tabs defaultValue="info">
                <TabsList className="w-full">
                  <TabsTrigger value="info" className="flex-1">
                    Информация
                  </TabsTrigger>
                  <TabsTrigger value="history" className="flex-1">
                    История ремонта
                  </TabsTrigger>
                </TabsList>

                <TabsContent value="info" className="pt-4">
                  <div className="space-y-6">
                    <div>
                      <h3 className="text-lg font-medium">
                        {car.brand} {car.model}{" "}
                        <span className="text-muted-foreground ml-1">
                          {car.year} г.
                        </span>
                      </h3>
                    </div>

                    <Separator />

                    <div>
                      <h4 className="mb-2 text-sm font-medium">Владелец</h4>
                      {car.client ? (
                        <div className="space-y-2">
                          <p className="font-medium">
                            {car.client.last_name} {car.client.first_name}
                          </p>
                          <div className="grid grid-cols-2 gap-2 text-sm">
                            <p className="text-muted-foreground">Телефон:</p>
                            <p>{car.client.phone}</p>
                            {car.client.email && (
                              <>
                                <p className="text-muted-foreground">Email:</p>
                                <p>{car.client.email}</p>
                              </>
                            )}
                          </div>
                        </div>
                      ) : (
                        <p className="text-muted-foreground text-sm">
                          Владелец не указан
                        </p>
                      )}
                    </div>

                    <Separator />

                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <p className="text-muted-foreground text-sm">
                          Гос. номер
                        </p>
                        <p className="font-medium">{car.license_plate}</p>
                      </div>
                      <div>
                        <p className="text-muted-foreground text-sm">
                          Страна регистрации
                        </p>
                        <p className="font-medium">{countryName}</p>
                      </div>
                    </div>

                    <Separator />

                    <div>
                      <p className="text-muted-foreground text-sm">VIN</p>
                      <p className="font-medium">{car.vin}</p>
                    </div>

                    {car.frame && (
                      <div>
                        <p className="text-muted-foreground text-sm">
                          Номер кузова
                        </p>
                        <p className="font-medium">{car.frame}</p>
                      </div>
                    )}

                    <Separator />

                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <p className="text-muted-foreground text-sm">Пробег</p>
                        <p className="font-medium">{car.mileage} км</p>
                      </div>
                      <div>
                        <p className="text-muted-foreground text-sm">Цвет</p>
                        <div className="flex items-center gap-2">
                          {car.color ? (
                            <>
                              <div
                                className="h-4 w-4 rounded-full border border-gray-300"
                                style={{ backgroundColor: car.color.hex_code }}
                              />
                              <p className="font-medium">{car.color.name}</p>
                            </>
                          ) : (
                            <p className="font-medium">Не указан</p>
                          )}
                        </div>
                      </div>
                    </div>

                    <Separator />

                    <div className="grid grid-cols-2 gap-4">
                      <div>
                        <p className="text-muted-foreground text-sm">
                          Дата добавления
                        </p>
                        <p className="font-medium">
                          {new Date(car.created_at).toLocaleDateString("ru-RU")}
                        </p>
                      </div>
                      <div>
                        <p className="text-muted-foreground text-sm">
                          Последнее обновление
                        </p>
                        <p className="font-medium">
                          {new Date(car.updated_at).toLocaleDateString("ru-RU")}
                        </p>
                      </div>
                    </div>
                  </div>
                </TabsContent>

                <TabsContent value="history" className="pt-4">
                  <div className="flex flex-col items-center justify-center py-10 text-center">
                    <div className="bg-muted mb-4 rounded-full p-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-6 w-6"
                      >
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                      </svg>
                    </div>
                    <h3 className="mb-2 text-lg font-medium">
                      История ремонта пуста
                    </h3>
                    <p className="text-muted-foreground max-w-xs text-sm">
                      В будущем здесь будет отображаться история ремонта и
                      обслуживания автомобиля
                    </p>
                  </div>
                </TabsContent>
              </Tabs>
            </div>
          </ScrollArea>

          <SheetFooter className="border-t p-6">
            <div className="flex w-full justify-between">
              <div className="flex space-x-2">
                {onEdit && (
                  <Button variant="outline" onClick={() => onEdit(car)}>
                    <Edit className="mr-2 h-4 w-4" />
                    Редактировать
                  </Button>
                )}
                {onDelete && (
                  <Button
                    variant="outline"
                    onClick={() => setDeleteDialogOpen(true)}
                    className="text-destructive hover:text-destructive hover:bg-destructive/10"
                  >
                    <Trash className="mr-2 h-4 w-4" />
                    Удалить
                  </Button>
                )}
              </div>
              <Button onClick={() => handleSheetOpenChange(false)}>Закрыть</Button>
            </div>
          </SheetFooter>
        </SheetContent>
      </Sheet>
      
      <DeleteCar
        open={deleteDialogOpen} 
        onOpenChange={setDeleteDialogOpen}
        onConfirm={handleDelete}
        car={car}
      />
    </>
  );
} 