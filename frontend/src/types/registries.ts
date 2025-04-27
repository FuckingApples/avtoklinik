import type { LucideIcon } from "lucide-react";

export interface Color {
    id: string;
    name: string;
    hex?: string;
    code?: string | null;
}

export interface Manufacturer {
    id: string;
    name: string;
    description: string;
    created_at: string;
    updated_at: string;
}

export interface MeasurementUnit {
    id: string;
    unit: string;
    abbreviation: string;
    okei_code: string;
    created_at: string;
    updated_at: string;
}

export interface RegistryItem {
    title: string;
    path: string;
    href: (org_id: string) => string;
    count: number;
    icon: LucideIcon;
    buttonTitle: string;
    importEnabled?: boolean;
}

export interface RegistrySection {
    title: string;
    items: RegistryItem[];
}

export interface RegistriesCounts {
    categories: number;
    manufacturers: number;
    colors: number;
    measurement_units: number;
    workplaces: number;
    hourly_wages: number;
    equipments: number;
}