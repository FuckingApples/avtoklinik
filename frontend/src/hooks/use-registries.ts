import { useQuery, useMutation, keepPreviousData } from "@tanstack/react-query";
import { getManufacturers, getMeasurementUnits } from "~/api/registries";
import { useOrganizationStore } from "~/store/organization";
import { useManufacturersStore, useMeasurementUnitsStore } from "~/store/registries";

export const useManufacturers = () => {
    const { organization } = useOrganizationStore();
    const { filters } = useManufacturersStore();

    return useQuery({
        queryKey: ["manufacturers", organization?.id, filters],
        queryFn: async () => {
            if (!organization?.id) {
                throw new Error("Organization not selected");
            }
            return await getManufacturers(organization.id, filters);
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
            return await getMeasurementUnits(organization.id, filters);
        },
        enabled: !!organization?.id,
        staleTime: 1000 * 60,
        retry: false,
        placeholderData: keepPreviousData,
    });
};