import { useQuery, useMutation, keepPreviousData } from "@tanstack/react-query";
import { getRegistry } from "~/api/registries";
import { useOrganizationStore } from "~/store/organization";
import {
  GetEquipmentsFilters,
  GetHourlyWagesFilters,
  useEquipmentsStore,
  useHourlyWagesStore,
  useManufacturersStore,
  useMeasurementUnitsStore,
} from "~/store/registries";
import type {
  Equipment,
  HourlyWage,
  Manufacturer,
  MeasurementUnit,
} from "~/types/registries";
import type {
  GetManufacturersFilters,
  GetMeasurementUnitsFilters,
} from "~/store/registries";

export const useManufacturers = () => {
  const { organization } = useOrganizationStore();
  const { filters } = useManufacturersStore();

  return useQuery({
    queryKey: ["manufacturers", organization?.id, filters],
    queryFn: async () => {
      if (!organization?.id) {
        throw new Error("Organization not selected");
      }
      return await getRegistry<Manufacturer, GetManufacturersFilters>(
        "manufacturers",
        organization.id,
        filters,
      );
    },
    enabled: !!organization?.id,
    staleTime: 1000 * 60,
    retry: false,
    placeholderData: keepPreviousData,
  });
};

export const useMeasurementUnits = () => {
  const { organization } = useOrganizationStore();
  const { filters } = useMeasurementUnitsStore();

  return useQuery({
    queryKey: ["measurement_units", organization?.id, filters],
    queryFn: async () => {
      if (!organization?.id) {
        throw new Error("Organization not selected");
      }
      return await getRegistry<MeasurementUnit, GetMeasurementUnitsFilters>(
        "measurement_units",
        organization.id,
        filters,
      );
    },
    enabled: !!organization?.id,
    staleTime: 1000 * 60,
    retry: false,
    placeholderData: keepPreviousData,
  });
};

export const useHourlyWages = () => {
  const { organization } = useOrganizationStore();
  const { filters } = useHourlyWagesStore();

  return useQuery({
    queryKey: ["hourly_wages", organization?.id, filters],
    queryFn: async () => {
      if (!organization?.id) {
        throw new Error("Organization not selected");
      }
      return await getRegistry<HourlyWage, GetHourlyWagesFilters>(
        "hourly_wages",
        organization.id,
        filters,
      );
    },
    enabled: !!organization?.id,
    staleTime: 1000 * 60,
    retry: false,
    placeholderData: keepPreviousData,
  });
};

export const useEquipments = () => {
  const { organization } = useOrganizationStore();
  const { filters } = useEquipmentsStore();

  return useQuery({
    queryKey: ["equipments", organization?.id, filters],
    queryFn: async () => {
      if (!organization?.id) {
        throw new Error("Organization not selected");
      }
      return await getRegistry<Equipment, GetEquipmentsFilters>(
        "equipments",
        organization.id,
        filters,
      );
    },
    enabled: !!organization?.id,
    staleTime: 1000 * 60,
    retry: false,
    placeholderData: keepPreviousData,
  });
};
