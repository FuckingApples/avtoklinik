import type { Organization } from "~/types/organization";
import { create } from "zustand";

type OrganizationState = {
  organization: Organization | null;
  setOrganization: (organization: Organization) => void;
  clearOrganization: () => void;
};

export const useOrganizationStore = create<OrganizationState>((set) => ({
  organization: null,
  setOrganization: (organization) => set({ organization }),
  clearOrganization: () => set({ organization: null }),
}));
