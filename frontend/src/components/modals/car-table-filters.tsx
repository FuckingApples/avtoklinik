"use client";

import { useState, useEffect } from "react";
import { X, Filter as FilterIcon, ChevronDown } from "lucide-react";
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
import { Badge } from "~/components/ui/badge";
import { CarFilterOptions } from "~/types/car";
import { COUNTRIES } from "~/api/registries";

interface CarFiltersProps {
  open: boolean;
  onClose: () => void;
  filterOptions: CarFilterOptions;
  initialFilters: Record<string, any>;
  onApplyFilters: (filters: Record<string, any>) => void;
}

export function CarFiltersDialog({
  open,
  onClose,
  filterOptions,
  initialFilters,
  onApplyFilters
}: CarFiltersProps) {
  const [filters, setFilters] = useState<Record<string, any>>(initialFilters);

  useEffect(() => {
    if (open) {
      setFilters(initialFilters);
    }
  }, [open, initialFilters]);
  
  const handleInputChange = (key: string, value: any) => {
    setFilters(prev => ({
      ...prev,
      [key]: value
    }));
  };
  
  const handleApply = () => {
    onApplyFilters(filters);
    onClose();
  };
  
  const handleReset = () => {
    setFilters({});
  };

  const activeFilterCount = Object.keys(filters).length;

  return (
    <Dialog open={open} onOpenChange={(isOpen) => !isOpen && onClose()}>
      <DialogContent className="sm:max-w-[500px]">
        <DialogHeader>
          <div className="flex h-7 items-center">
            <DialogTitle>Фильтры</DialogTitle>
            <div className="ml-3 h-5">
              {activeFilterCount > 0 ? (
                <Badge
                  variant="secondary"
                  className="flex items-center justify-center px-2 py-0.5 text-xs"
                >
                  {activeFilterCount}{" "}
                  {activeFilterCount === 1
                    ? "фильтр"
                    : activeFilterCount < 5
                      ? "фильтра"
                      : "фильтров"}
                </Badge>
              ) : null}
            </div>
          </div>
        </DialogHeader>

        <Separator className="my-4" />

        <ScrollArea className="h-[400px] pr-6">
          <div className="relative space-y-6 px-1 pb-2">
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="brand">Марка</Label>
                <div className="relative">
                  <select
                    id="brand"
                    className="border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50"
                    value={filters.brand || ""}
                    onChange={(e) =>
                      handleInputChange("brand", e.target.value)
                    }
                  >
                    <option value="">Все марки</option>
                    {filterOptions.brands.map((brand) => (
                      <option key={brand} value={brand}>
                        {brand}
                      </option>
                    ))}
                  </select>
                  <ChevronDown className="text-muted-foreground pointer-events-none absolute top-1/2 right-2.5 h-4 w-4 -translate-y-1/2" />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="model">Модель</Label>
                <div className="relative">
                  <select
                    id="model"
                    className="border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50"
                    value={filters.model || ""}
                    onChange={(e) =>
                      handleInputChange("model", e.target.value)
                    }
                    disabled={filterOptions.models.length === 0}
                  >
                    <option value="">Все модели</option>
                    {filterOptions.models.map((model) => (
                      <option key={model} value={model}>
                        {model}
                      </option>
                    ))}
                  </select>
                  <ChevronDown className="text-muted-foreground pointer-events-none absolute top-1/2 right-2.5 h-4 w-4 -translate-y-1/2" />
                </div>
              </div>
            </div>

            <div className="space-y-2">
              <Label>Год</Label>
              <div className="grid grid-cols-2 gap-4">
                <Input
                  id="yearFrom"
                  type="number"
                  min={filterOptions.yearRange[0]}
                  max={filterOptions.yearRange[1]}
                  placeholder="От"
                  value={filters.yearFrom || ""}
                  onChange={(e) =>
                    handleInputChange("yearFrom", e.target.value)
                  }
                />
                <Input
                  id="yearTo"
                  type="number"
                  min={filterOptions.yearRange[0]}
                  max={filterOptions.yearRange[1]}
                  placeholder="До"
                  value={filters.yearTo || ""}
                  onChange={(e) =>
                    handleInputChange("yearTo", e.target.value)
                  }
                />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="color">Цвет</Label>
              <div className="relative">
                <select
                  id="color"
                  className="border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50"
                  value={filters.color || ""}
                  onChange={(e) => handleInputChange("color", e.target.value)}
                  disabled={filterOptions.colors.length === 0}
                >
                  <option value="">Все цвета</option>
                  {filterOptions.colors.map((color) => (
                    <option key={color.id} value={color.id}>
                      {color.name}
                    </option>
                  ))}
                </select>
                <ChevronDown className="text-muted-foreground pointer-events-none absolute top-1/2 right-2.5 h-4 w-4 -translate-y-1/2" />
              </div>
            </div>

            <div className="space-y-2">
              <Label>Пробег</Label>
              <div className="grid grid-cols-2 gap-4">
                <Input
                  id="mileageFrom"
                  type="number"
                  min={0}
                  placeholder="От"
                  value={filters.mileageFrom || ""}
                  onChange={(e) =>
                    handleInputChange("mileageFrom", e.target.value)
                  }
                />
                <Input
                  id="mileageTo"
                  type="number"
                  min={0}
                  placeholder="До"
                  value={filters.mileageTo || ""}
                  onChange={(e) =>
                    handleInputChange("mileageTo", e.target.value)
                  }
                />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="license_plate_region">Страна регистрации</Label>
              <div className="relative mx-0 mb-2">
                <select
                  id="license_plate_region"
                  className="border-input bg-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-9 w-full appearance-none rounded-md border py-1 pr-8 pl-3 text-sm shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-1 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50"
                  value={filters.license_plate_region || ""}
                  onChange={(e) =>
                    handleInputChange("license_plate_region", e.target.value)
                  }
                >
                  <option value="">Все страны</option>
                  {COUNTRIES.map((country) => (
                    <option key={country.code} value={country.code}>
                      {country.name}
                    </option>
                  ))}
                </select>
                <ChevronDown className="text-muted-foreground pointer-events-none absolute top-1/2 right-2.5 h-4 w-4 -translate-y-1/2" />
              </div>
            </div>
          </div>
        </ScrollArea>

        <DialogFooter className="mt-6 flex justify-between">
          <div className="flex gap-2">
            <Button
              variant="outline"
              onClick={handleReset}
              disabled={activeFilterCount === 0}
              className="inline-flex items-center"
            >
              <span className="flex items-center pr-2">
                <X className="mr-1.5 size-4" />
                Сбросить
              </span>
            </Button>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" onClick={onClose}>
              Отмена
            </Button>
            <Button
              onClick={handleApply}
              disabled={
                activeFilterCount === 0 &&
                Object.keys(initialFilters).length === 0
              }
              className="inline-flex items-center"
            >
              <span className="flex items-center pr-2">
                <FilterIcon className="mr-1.5 size-4" />
                Применить
              </span>
            </Button>
          </div>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
} 