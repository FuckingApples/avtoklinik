import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { createOrganization, getOrganizationInfo } from "~/api/organization";
import { toast } from "sonner";
import { useRouter } from "next/navigation";
import { useOrganizationStore } from "~/store/organization";

export const useOrganization = (params: {
  id: number | null;
  enabled?: boolean;
}) => {
  const { setOrganization } = useOrganizationStore();

  return useQuery({
    queryKey: ["organization", params.id],
    queryFn: async () => {
      if (!params.id) throw new Error("No id provided");
      const data = await getOrganizationInfo(params.id);
      setOrganization(data);
      return data;
    },
    staleTime: 1000 * 60 * 30, // Кэш 30 минут
    enabled: params.enabled,
  });
};

export const useCreateOrganization = () => {
  const queryClient = useQueryClient();
  const router = useRouter();

  return useMutation({
    mutationFn: createOrganization,
    onSuccess: async (data) => {
      await queryClient.invalidateQueries({
        queryKey: ["user"],
      });
      await queryClient.refetchQueries({ queryKey: ["user"] });
      toast.success("Организация создана");
      router.push(`/dashboard/org/${data.public_id}`);
    },
  });
};
