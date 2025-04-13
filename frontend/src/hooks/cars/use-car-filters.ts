import { useState, useEffect } from "react";
import { Car, CarFilterOptions, Color } from "~/types/car";

const INITIAL_FILTER_OPTIONS: CarFilterOptions = {
  brands: [],
  models: [],
  yearRange: [new Date().getFullYear() - 30, new Date().getFullYear()],
  colors: []
};

export function useCarFilters(cars: Car[]) {
  const [filterOptions, setFilterOptions] = useState<CarFilterOptions>(INITIAL_FILTER_OPTIONS);
  const [filters, setFilters] = useState<Record<string, any>>({});
  const [filteredCars, setFilteredCars] = useState<Car[]>(cars);

  useEffect(() => {
    if (cars.length === 0) {
      setFilterOptions(INITIAL_FILTER_OPTIONS);
      return;
    }

    const brands = Array.from(new Set(cars.map(car => car.brand))).sort();
    const models = Array.from(new Set(cars.map(car => car.model))).sort();
    
    const years = cars.map(car => car.year);
    const minYear = Math.min(...years);
    const maxYear = Math.max(...years);
    const yearRange: [number, number] = [
      minYear > 0 ? minYear : INITIAL_FILTER_OPTIONS.yearRange[0],
      maxYear > 0 ? maxYear : INITIAL_FILTER_OPTIONS.yearRange[1]
    ];
    
    const uniqueColors: Color[] = [];
    const colorIds = new Set<string>();
    
    cars.forEach(car => {
      if (car.color && !colorIds.has(car.color.id)) {
        colorIds.add(car.color.id);
        uniqueColors.push(car.color);
      }
    });

    setFilterOptions({
      brands,
      models,
      yearRange,
      colors: uniqueColors.sort((a, b) => a.name.localeCompare(b.name))
    });
  }, [cars]);

  useEffect(() => {
    if (Object.keys(filters).length === 0) {
      setFilteredCars(cars);
      return;
    }

    const filtered = cars.filter(car => {
      if (filters.brand && car.brand !== filters.brand) {
        return false;
      }

      if (filters.model && car.model !== filters.model) {
        return false;
      }

      if (filters.yearFrom && car.year < parseInt(filters.yearFrom)) {
        return false;
      }
      if (filters.yearTo && car.year > parseInt(filters.yearTo)) {
        return false;
      }

      if (filters.color && (!car.color || car.color.id !== filters.color)) {
        return false;
      }

      if (filters.mileageFrom && car.mileage < parseInt(filters.mileageFrom)) {
        return false;
      }
      if (filters.mileageTo && car.mileage > parseInt(filters.mileageTo)) {
        return false;
      }

      if (filters.license_plate_region && car.license_plate_region !== filters.license_plate_region) {
        return false;
      }

      return true;
    });

    setFilteredCars(filtered);
  }, [filters, cars]);

  useEffect(() => {
    if (Object.keys(filters).length === 0) {
      setFilteredCars(cars);
    }
  }, [cars]);

  const applyFilters = (newFilters: Record<string, any>) => {
    const cleanedFilters = Object.fromEntries(
      Object.entries(newFilters).filter(([_, value]) => 
        value !== null && value !== undefined && value !== ''
      )
    );
    
    setFilters(cleanedFilters);
  };

  const resetFilters = () => {
    setFilters({});
  };

  return {
    filters,
    filterOptions,
    applyFilters,
    resetFilters,
    filteredCars
  };
} 