import { useQuery, useMutation, keepPreviousData } from "@tanstack/react-query";
import { getManufacturers } from "~/api/registries";
import { useOrganizationStore } from "~/store/organization";
import { useManufacturersStore } from "~/store/registries";

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
