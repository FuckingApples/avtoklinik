"use client";

import { useState, useEffect, useCallback } from "react";
import { useParams } from "next/navigation";
import { SidebarTrigger } from "~/components/ui/sidebar";
import { Separator } from "~/components/ui/separator";
import { Button } from "~/components/ui/button";
import { Settings, Filter, Plus, Car as CarIcon, Search } from "lucide-react";
import { Car } from "~/types/car";
import { Cars } from "~/components/tables/cars";
import { CarDetails } from "~/components/sidebars/car-details";
import { CarTableSettingsDialog } from "~/components/modals/car-table-settings";
import { CarFiltersDialog } from "~/components/modals/car-table-filters";
import { CarForm } from "~/components/modals/car-record";
import { DeleteCar } from "~/components/modals/delete-car";
import { useCarTableSettings } from "~/hooks/cars/use-car-table-settings";
import { useCarFilters } from "~/hooks/cars/use-car-filters";
import { toast } from "sonner";
import { Badge } from "~/components/ui/badge";
import { getCars, createCar, updateCar, deleteCar, getCar } from "~/api/cars";
import { getCountryName } from "~/api/registries";

export default function CarsPage() {
  const { org_id } = useParams();
  const [cars, setCars] = useState<Car[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedCar, setSelectedCar] = useState<Car | null>(null);
  const [isDetailSidebarOpen, setIsDetailSidebarOpen] = useState(false);
  const [isTableSettingsOpen, setIsTableSettingsOpen] = useState(false);
  const [isFiltersOpen, setIsFiltersOpen] = useState(false);
  const [isCarFormOpen, setIsCarFormOpen] = useState(false);
  const [editingCar, setEditingCar] = useState<Car | null>(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [carToDelete, setCarToDelete] = useState<string | null>(null);
  
  const { settings, saveSettings } = useCarTableSettings(org_id as string);
  const { 
    filters, 
    filterOptions, 
    applyFilters,
    filteredCars 
  } = useCarFilters(cars);

  useEffect(() => {
    fetchCars();
  }, [org_id]);

  const fetchCars = async () => {
    setLoading(true);
    try {
      const data = await getCars(org_id as string);
      setCars(data);
    } catch (error) {
      toast.error("Не удалось загрузить список автомобилей");
      setCars([]);
    } finally {
      setLoading(false);
    }
  };

  const handleCarSelect = (car: Car) => {
    setSelectedCar(car);
    setIsDetailSidebarOpen(true);
  };

  const handleDetailSidebarClose = () => {
    setIsDetailSidebarOpen(false);
  };

  const handleDeleteCar = useCallback((carId: string) => {
    setCarToDelete(carId);
    setDeleteDialogOpen(true);
  }, []);

  const confirmDeleteCar = useCallback(async () => {
    if (!carToDelete) return;
    
    try {
      await deleteCar(org_id as string, carToDelete);
      setCars(prevCars => prevCars.filter(car => car.id !== carToDelete));
      toast.success("Автомобиль успешно удален");

      if (selectedCar?.id === carToDelete) {
        setIsDetailSidebarOpen(false);
      }
    } catch (error) {
      toast.error('Не удалось удалить автомобиль. Пожалуйста, попробуйте снова');
    } finally {
      setDeleteDialogOpen(false);
      setCarToDelete(null);
    }
  }, [carToDelete, org_id, selectedCar]);

  const handleEditCar = (car: Car) => {
    setEditingCar(car);
    setIsCarFormOpen(true);
  };

  const handleAddCar = () => {
    setEditingCar(null);
    setIsCarFormOpen(true);
  };

  const handleCarFormSubmit = async (carData: Partial<Car>) => {
    try {
      const isEditing = !!editingCar;
      
      if (isEditing && editingCar) {
        const updatedCar = await updateCar(org_id as string, editingCar.id, carData);
        setCars(prevCars => 
          prevCars.map(car => car.id === editingCar.id ? updatedCar : car)
        );
        toast.success("Автомобиль успешно обновлен");
      } else {
        const newCar = await createCar(org_id as string, carData);
        setCars(prevCars => [...prevCars, newCar]);
        toast.success("Автомобиль успешно добавлен");
      }

    } catch (error) {
      toast.error(
        `Не удалось ${editingCar ? 'обновить' : 'добавить'} автомобиль. ${(error as Error).message}`
      );
      throw error;
    }
  };

  const getFilteredCars = () => {
    let carsToFilter = filteredCars;

    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase().trim();
      carsToFilter = carsToFilter.filter(car => {
        const countryName = getCountryName(car.license_plate_region || "").toLowerCase();

        const matchesCar = (car.brand?.toLowerCase().includes(query) || false) ||
            (car.model?.toLowerCase().includes(query) || false) ||
            (car.license_plate?.toLowerCase().includes(query) || false) ||
            (car.vin?.toLowerCase().includes(query) || false) ||
            (car.color?.name?.toLowerCase().includes(query) || false) ||
            (countryName.includes(query) || false);

        const matchesClient = car.client ? (
            (car.client.last_name?.toLowerCase().includes(query) || false) ||
            (car.client.first_name?.toLowerCase().includes(query) || false) ||
            (car.client.phone?.includes(query) || false) ||
            (`${car.client.last_name} ${car.client.first_name}`.toLowerCase().includes(query) || false)
        ) : false;

        return matchesCar || matchesClient;
      });
    }
    
    return carsToFilter;
  };

  const carInfo = carToDelete ? cars.find(car => car.id === carToDelete) : null;

  return (
    <div className="flex h-full flex-col">
      <header className="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12 border-b">
        <div className="flex items-center justify-between w-full px-6">
          <div className="flex items-center gap-2">
            <SidebarTrigger className="-ml-1" />
            <Separator orientation="vertical" className="mr-2 h-4" />
            <h1 className="text-xl font-semibold">Автомобили</h1>
          </div>
          
          <div className="flex items-center gap-3">
            <div className="flex relative w-[400px] items-center border rounded-md focus-within:ring-1 focus-within:ring-ring h-9 px-3">
              <Search className="h-4 w-4 text-muted-foreground mr-2 flex-shrink-0" />
              <input
                className="flex h-full w-full bg-transparent py-2 text-sm outline-none placeholder:text-muted-foreground disabled:cursor-not-allowed disabled:opacity-50"
                placeholder="Поиск по ВИН, номеру, марке..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              {searchQuery && (
                <button 
                  className="ml-1 h-5 w-5 rounded-full bg-muted flex items-center justify-center hover:bg-muted-foreground/20 flex-shrink-0"
                  onClick={() => setSearchQuery("")}
                >
                  <span className="sr-only">Очистить</span>
                  <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9 3L3 9M3 3L9 9" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                </button>
              )}
            </div>
            
            <Button 
              variant="outline" 
              size="sm"
              onClick={() => setIsFiltersOpen(true)}
              className="h-9 inline-flex items-center"
            >
              <span className="flex items-center pr-2">
                <Filter className={Object.keys(filters).length > 0 ? "size-4 mr-1.5 text-primary" : "size-4 mr-1.5"} />
                Фильтры
                {Object.keys(filters).length > 0 && (
                  <Badge variant="secondary" className="ml-1.5 h-5 px-1.5 py-0 text-xs">
                    {Object.keys(filters).length}
                  </Badge>
                )}
              </span>
            </Button>
            <Button 
              variant="outline" 
              size="sm"
              onClick={() => setIsTableSettingsOpen(true)}
              className="h-9 inline-flex items-center"
            >
              <span className="flex items-center pr-2">
                <Settings className="size-4 mr-1.5" />
                Настройки таблицы
              </span>
            </Button>
            <Button 
              size="sm"
              onClick={handleAddCar}
              className="h-9 inline-flex items-center"
            >
              <span className="flex items-center pr-2">
                <Plus className="size-4 mr-1.5" />
                Добавить автомобиль
              </span>
            </Button>
          </div>
        </div>
      </header>
      
      <main className="flex-1 px-6 py-6">
        {loading ? (
          <div className="flex items-center justify-center h-40">
            <p className="text-muted-foreground">Загрузка данных...</p>
          </div>
        ) : cars.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-[calc(100vh-300px)] py-10 text-center">
            <div className="rounded-full bg-muted p-4 mb-4">
              <CarIcon className="h-6 w-6" />
            </div>
            <h3 className="text-xl font-medium mb-2">Нет автомобилей</h3>
            <p className="text-muted-foreground text-sm max-w-md mb-5">
              У вас пока нет добавленных автомобилей. Нажмите на кнопку ниже, чтобы создать первую запись.
            </p>
            <Button onClick={handleAddCar} className="inline-flex items-center">
              <span className="flex items-center pr-2">
                <Plus className="size-4 mr-1.5" />
                Добавить автомобиль
              </span>
            </Button>
          </div>
        ) : (
          <div className="border rounded-md overflow-hidden">
            <Cars
              onCarSelect={handleCarSelect} 
              visibleColumns={settings.columns}
              cars={getFilteredCars()}
              onDelete={handleDeleteCar}
              onEdit={handleEditCar}
              pageSize={settings.pageSize}
            />
          </div>
        )}
      </main>

      {isDetailSidebarOpen && (
        <CarDetails
          car={selectedCar} 
          open={isDetailSidebarOpen} 
          onClose={handleDetailSidebarClose} 
          orgId={org_id as string}
          onEdit={handleEditCar}
          onDelete={handleDeleteCar}
        />
      )}

      <CarTableSettingsDialog 
        open={isTableSettingsOpen}
        onClose={() => setIsTableSettingsOpen(false)}
        settings={settings}
        onSave={saveSettings}
      />

      <CarFiltersDialog 
        open={isFiltersOpen}
        onClose={() => setIsFiltersOpen(false)}
        filterOptions={filterOptions}
        initialFilters={filters}
        onApplyFilters={applyFilters}
      />

      <CarForm
        open={isCarFormOpen}
        onClose={() => setIsCarFormOpen(false)}
        onSubmit={async (carData) => {
          await handleCarFormSubmit(carData);

          if (editingCar && selectedCar && editingCar.id === selectedCar.id) {
            const updatedCar = await getCar(org_id as string, editingCar.id);
            setSelectedCar(updatedCar);
          }
        }}
        car={editingCar}
        orgId={org_id as string}
      />

      <DeleteCar
        open={deleteDialogOpen}
        onOpenChange={setDeleteDialogOpen}
        onConfirm={confirmDeleteCar}
        car={carInfo}
      />
    </div>
  );
} 