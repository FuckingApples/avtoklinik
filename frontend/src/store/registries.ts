import type { PaginationParams, BaseFiltersParams } from "~/types/api";
import { create } from "zustand";

export type GetManufacturersFilters = BaseFiltersParams & PaginationParams & {};

type ManufacturersState = {
  filters?: GetManufacturersFilters;
  setFilters: (filters?: GetManufacturersFilters) => void;
};

export const useManufacturersStore = create<ManufacturersState>((set) => ({
  filters: undefined,
  pagination: undefined,
  setFilters: (filters) => set({ filters }),
}));

export type GetMeasurementUnitsFilters = BaseFiltersParams &
  PaginationParams & {};

type MeasurementUnitsState = {
  filters?: GetMeasurementUnitsFilters;
  setFilters: (filters?: GetMeasurementUnitsFilters) => void;
};

export const useMeasurementUnitsStore = create<MeasurementUnitsState>(
  (set) => ({
    filters: undefined,
    pagination: undefined,
    setFilters: (filters) => set({ filters }),
  }),
);

export type GetHourlyWagesFilters = BaseFiltersParams & PaginationParams & {};

type HourlyWagesState = {
  filters?: GetHourlyWagesFilters;
  setFilters: (filters?: GetHourlyWagesFilters) => void;
};

export const useHourlyWagesStore = create<HourlyWagesState>((set) => ({
  filters: undefined,
  pagination: undefined,
  setFilters: (filters) => set({ filters }),
}));

export type GetEquipmentsFilters = BaseFiltersParams & PaginationParams & {};

type EquipmentsState = {
  filters?: GetEquipmentsFilters;
  setFilters: (filters?: GetEquipmentsFilters) => void;
};

export const useEquipmentsStore = create<EquipmentsState>((set) => ({
  filters: undefined,
  pagination: undefined,
  setFilters: (filters) => set({ filters }),
}));
