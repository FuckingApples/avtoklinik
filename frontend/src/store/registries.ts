import type { PaginationParams, BaseFiltersParams } from "~/types/api";
import { create } from "zustand";

export type GetManufacturersFilters = BaseFiltersParams &
    PaginationParams & {
};

type ManufacturersState = {
    filters?: GetManufacturersFilters;
    setFilters: (filters?: GetManufacturersFilters) => void;
};

export const useManufacturersStore = create<ManufacturersState>((set) => ({
    filters: undefined,
    pagination: undefined,
    setFilters: (filters) => set({ filters }),
}));
