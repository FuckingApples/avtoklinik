import type { Organization } from "~/types/organization";

export type User = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  is_email_verified: boolean;
  organizations: Organization[];
};
