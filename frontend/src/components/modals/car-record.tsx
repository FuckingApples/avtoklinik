"use client";

import { useState, useEffect } from "react";
import { Car, Color } from "~/types/car";
import { 
  Dialog, 
  DialogContent, 
  DialogHeader, 
  DialogTitle, 
  DialogFooter 
} from "~/components/ui/dialog";
import { Button } from "~/components/ui/button";
import { Label } from "~/components/ui/label";
import { Input } from "~/components/ui/input";
import { Separator } from "~/components/ui/separator";
import { ScrollArea } from "~/components/ui/scroll-area";
import { Loader2 } from "lucide-react";
import { toast } from "sonner";
import { getColors } from "~/api/registries";
import { getCountries, Country } from "~/api/registries";
import { getClients } from "~/api/clients";
import { Client } from "~/api/clients";
import { cn } from "~/lib/utils";

export interface CarFormProps {
  open: boolean;
  onClose: () => void;
  onSubmit: (car: Partial<Car>) => Promise<void>;
  car?: Car | null;
  orgId: string;
}

export function CarForm({ open, onClose, onSubmit, car, orgId }: CarFormProps) {
  const [loading, setLoading] = useState(false);
  const [colors, setColors] = useState<Color[]>([]);
  const [countries, setCountries] = useState<Country[]>([]);
  const [clients, setClients] = useState<Client[]>([]);
  const [selectedColorId, setSelectedColorId] = useState<string>("");
  const [formData, setFormData] = useState<Partial<Car & {client_id?: string}>>({
    brand: "",
    model: "",
    year: new Date().getFullYear(),
    vin: "",
    frame: null,
    license_plate: "",
    license_plate_region: "RU",
    mileage: 0,
    color: null,
    client_id: undefined
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  useEffect(() => {
    async function fetchData() {
      if (!open) return;

      setLoading(true);
      try {
        const colorData = await getColors(orgId);
        setColors(colorData);

        const countryData = await getCountries();
        setCountries(countryData);

        const clientData = await getClients(orgId);
        setClients(clientData);
      } catch (error) {
        toast.error("Не удалось загрузить данные автомобиля");
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [open, orgId]);

  useEffect(() => {
    if (open) {
      if (car) {
        setFormData({
          brand: car.brand || "",
          model: car.model || "",
          year: car.year || new Date().getFullYear(),
          vin: car.vin || "",
          frame: car.frame,
          license_plate: car.license_plate || "",
          license_plate_region: car.license_plate_region || "RU",
          mileage: car.mileage || 0,
          color: car.color,
          client_id: car.client?.id,
        });

        if (car.color) {
          setSelectedColorId(car.color.id);
        } else {
          setSelectedColorId("");
        }
      } else {
        setFormData({
          brand: "",
          model: "",
          year: new Date().getFullYear(),
          vin: "",
          frame: null,
          license_plate: "",
          license_plate_region: "RU",
          mileage: 0,
          color: null,
          client_id: undefined,
        });
        setSelectedColorId("");
      }
      setErrors({});
    }
  }, [open, car]);

  const handleInputChange = (
    key: keyof (Car & { client_id?: string }),
    value: any,
  ) => {
    setFormData((prev) => ({
      ...prev,
      [key]: value,
    }));

    if (errors[key]) {
      setErrors((prev) => {
        const newErrors = { ...prev };
        delete newErrors[key];
        return newErrors;
      });
    }
  };

  const validateForm = (): boolean => {
    const newErrors: Record<string, string> = {};

    if (!formData.brand) {
      newErrors.brand = "Марка обязательна";
    }

    if (!formData.model) {
      newErrors.model = "Модель обязательна";
    }

    if (!formData.vin) {
      newErrors.vin = "VIN обязателен";
    } else if (formData.vin.length !== 17) {
      newErrors.vin = "VIN должен содержать ровно 17 символов";
    }

    if (!formData.license_plate) {
      newErrors.license_plate = "Гос. номер обязателен";
    } else if (formData.license_plate.length < 5) {
      newErrors.license_plate =
        "Гос. номер должен содержать минимум 5 символов";
    }

    if (!formData.license_plate_region) {
      newErrors.license_plate_region = "Страна регистрации обязательна";
    }

    if (!formData.year) {
      newErrors.year = "Год обязателен";
    } else if (
      formData.year < 1900 ||
      formData.year > new Date().getFullYear() + 1
    ) {
      newErrors.year = `Год должен быть между 1900 и ${new Date().getFullYear() + 1}`;
    }

    if (formData.mileage === undefined || formData.mileage === null) {
      newErrors.mileage = "Пробег обязателен";
    } else if (formData.mileage < 0) {
      newErrors.mileage = "Пробег не может быть отрицательным";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async () => {
    if (!validateForm()) {
      return;
    }

    setLoading(true);
    try {
      const submitData: any = {
        brand: formData.brand,
        model: formData.model,
        year: formData.year,
        vin: formData.vin || undefined,
        frame: formData.frame === "" ? null : formData.frame,
        license_plate: formData.license_plate,
        license_plate_region: formData.license_plate_region,
        mileage: formData.mileage,
        client_id: formData.client_id,
      };

      if (selectedColorId) {
        submitData.color_id = selectedColorId;
      }

      Object.keys(submitData).forEach((key) => {
        if (submitData[key] === undefined) {
          delete submitData[key];
        }
      });

      await onSubmit(submitData);
      onClose();
    } catch (error) {
      console.error("Failed to submit car:", error);
      toast.error(
        `Не удалось ${car ? "обновить" : "создать"} автомобиль: ${(error as Error).message}`,
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={(isOpen) => !isOpen && onClose()}>
      <DialogContent className="sm:max-w-[550px]">
        <DialogHeader>
          <DialogTitle>
            {car ? "Редактировать автомобиль" : "Добавить автомобиль"}
          </DialogTitle>
        </DialogHeader>

        <Separator className="my-4" />

        <ScrollArea className="max-h-[400px] overflow-visible pr-6">
          <div className="space-y-6 px-1 pb-4">
            <div className="space-y-2">
              <Label htmlFor="client_id" className="flex items-center">
                Владелец
              </Label>
              <select
                id="client_id"
                className={cn(
                  "border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50",
                  errors.client_id && "border-destructive",
                )}
                value={formData.client_id || ""}
                onChange={(e) =>
                  handleInputChange("client_id", e.target.value)
                }
              >
                <option value="">Выберите владельца</option>
                {clients.map((client) => (
                  <option key={client.id} value={client.id}>
                    {client.last_name} {client.first_name} ({client.phone})
                  </option>
                ))}
              </select>
              {errors.client_id && (
                <p className="text-destructive text-xs">{errors.client_id}</p>
              )}
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="brand" className="flex items-center">
                  Марка <span className="text-destructive ml-1">*</span>
                </Label>
                <Input
                  id="brand"
                  placeholder="Например: Toyota"
                  value={formData.brand || ""}
                  onChange={(e) => handleInputChange("brand", e.target.value)}
                  className={errors.brand ? "border-destructive" : ""}
                />
                {errors.brand && (
                  <p className="text-destructive text-xs">{errors.brand}</p>
                )}
              </div>

              <div className="space-y-2">
                <Label htmlFor="model" className="flex items-center">
                  Модель <span className="text-destructive ml-1">*</span>
                </Label>
                <Input
                  id="model"
                  placeholder="Например: Camry"
                  value={formData.model || ""}
                  onChange={(e) => handleInputChange("model", e.target.value)}
                  className={errors.model ? "border-destructive" : ""}
                />
                {errors.model && (
                  <p className="text-destructive text-xs">{errors.model}</p>
                )}
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="year" className="flex items-center">
                  Год <span className="text-destructive ml-1">*</span>
                </Label>
                <Input
                  id="year"
                  type="number"
                  min={1900}
                  max={new Date().getFullYear() + 1}
                  value={formData.year || ""}
                  onChange={(e) =>
                    handleInputChange("year", parseInt(e.target.value))
                  }
                  className={errors.year ? "border-destructive" : ""}
                />
                {errors.year && (
                  <p className="text-destructive text-xs">{errors.year}</p>
                )}
              </div>

              <div className="space-y-2">
                <Label htmlFor="color">Цвет</Label>
                <select
                  id="color"
                  className="border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50"
                  value={selectedColorId}
                  onChange={(e) => {
                    const selectedColor = colors.find(
                      (c) => c.id === e.target.value,
                    );
                    handleInputChange("color", selectedColor || null);
                    setSelectedColorId(e.target.value);
                  }}
                >
                  <option value="">Выберите цвет</option>
                  {colors.map((color) => (
                    <option key={color.id} value={color.id}>
                      {color.name}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="vin" className="flex items-center">
                VIN <span className="text-destructive ml-1">*</span>
              </Label>
              <Input
                id="vin"
                placeholder="Например: 1HGCM82633A123456"
                value={formData.vin || ""}
                onChange={(e) => handleInputChange("vin", e.target.value)}
                maxLength={17}
                className={errors.vin ? "border-destructive" : ""}
              />
              {errors.vin && (
                <p className="text-destructive text-xs">{errors.vin}</p>
              )}
            </div>

            <div className="space-y-2">
              <Label htmlFor="frame">Номер кузова</Label>
              <Input
                id="frame"
                placeholder="Например: ABC123456"
                value={formData.frame || ""}
                onChange={(e) => handleInputChange("frame", e.target.value || null)}
              />
            </div>

            <div className="grid grid-cols-4 gap-4">
              <div className="col-span-3 space-y-2">
                <Label htmlFor="license_plate" className="flex items-center">
                  Гос. номер <span className="text-destructive ml-1">*</span>
                </Label>
                <Input
                  id="license_plate"
                  placeholder="Например: А123ВС77"
                  value={formData.license_plate || ""}
                  onChange={(e) =>
                    handleInputChange("license_plate", e.target.value)
                  }
                  className={errors.license_plate ? "border-destructive" : ""}
                />
                {errors.license_plate && (
                  <p className="text-destructive text-xs">
                    {errors.license_plate}
                  </p>
                )}
              </div>

              <div className="space-y-2">
                <Label
                  htmlFor="license_plate_region"
                  className="flex items-center"
                >
                  Страна <span className="text-destructive ml-1">*</span>
                </Label>
                <select
                  id="license_plate_region"
                  className={cn(
                    "border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50",
                    errors.license_plate_region && "border-destructive",
                  )}
                  value={formData.license_plate_region || ""}
                  onChange={(e) =>
                    handleInputChange("license_plate_region", e.target.value)
                  }
                >
                  {countries.map((country) => (
                    <option key={country.code} value={country.code}>
                      {country.name}
                    </option>
                  ))}
                </select>
                {errors.license_plate_region && (
                  <p className="text-destructive text-xs">
                    {errors.license_plate_region}
                  </p>
                )}
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="mileage" className="flex items-center">
                Пробег (км) <span className="text-destructive ml-1">*</span>
              </Label>
              <Input
                id="mileage"
                type="number"
                min={0}
                placeholder="Например: 15000"
                value={formData.mileage?.toString() || ""}
                onChange={(e) =>
                  handleInputChange("mileage", parseInt(e.target.value) || 0)
                }
                className={errors.mileage ? "border-destructive" : ""}
              />
              {errors.mileage && (
                <p className="text-destructive text-xs">{errors.mileage}</p>
              )}
            </div>
          </div>
        </ScrollArea>

        <DialogFooter className="mt-6">
          <Button variant="outline" onClick={onClose} disabled={loading}>
            Отмена
          </Button>
          <Button onClick={handleSubmit} disabled={loading}>
            {loading && <Loader2 className="mr-1.5 h-4 w-4 animate-spin" />}
            {car ? "Сохранить" : "Добавить"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
} 