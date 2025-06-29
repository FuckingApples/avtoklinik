import type { PaginationParams, BaseFiltersParams } from "~/types/api";
import { create } from "zustand";

export type GetCarsFilters = BaseFiltersParams &
  PaginationParams & {
    vin__icontains?: string;
  };

type CarsState = {
  filters?: GetCarsFilters;
  setFilters: (filters?: GetCarsFilters) => void;
};

export const useCarsStore = create<CarsState>((set) => ({
  filters: undefined,
  pagination: undefined,
  setFilters: (filters) => set({ filters }),
}));
