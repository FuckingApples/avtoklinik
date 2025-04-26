import type { Color } from "~/types/registries";

export interface CarOwner {
  id: string;
  first_name: string;
  last_name: string;
  phone: string;
  email?: string;
}

export interface Car {
  id: string;
  vin: string;
  frame: string | null;
  brand: string;
  model: string;
  year: number;
  color: Color | null;
  license_plate: string;
  license_plate_region: string;
  mileage: number;
  created_at: string;
  updated_at: string;
  client?: CarOwner | null;
}

export interface CarTableColumn {
  key: keyof Car | "actions";
  title: string;
  visible: boolean;
}

export interface CarTableSettings {
  columns: CarTableColumn[];
  pageSize: number;
}

export interface CarFilterOptions {
  brands: string[];
  models: string[];
  yearRange: [number, number];
  colors: Color[];
}
