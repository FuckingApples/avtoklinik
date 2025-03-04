"use client";

import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createOrganization } from "~/api/organization";
import { toast } from "sonner";
import { useRouter } from "next/navigation";

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
