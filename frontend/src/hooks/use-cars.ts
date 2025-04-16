import { useQuery, useMutation, keepPreviousData } from "@tanstack/react-query";
import { getCars } from "~/api/cars";
import { useOrganizationStore } from "~/store/organization";
import { useCarsStore } from "~/store/cars";

export const useCars = () => {
  const { organization } = useOrganizationStore();
  const { filters } = useCarsStore();

  return useQuery({
    queryKey: ["cars", organization?.id, filters],
    queryFn: async () => {
      if (!organization?.id) {
        throw new Error("Organization not selected");
      }
      return await getCars(organization.id, filters);
    },
    enabled: !!organization?.id,
    staleTime: 1000 * 60,
    retry: false,
    placeholderData: keepPreviousData,
  });
};
