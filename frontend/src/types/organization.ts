export type Organization = {
  id: number;
  public_id: string;
  name: string;
  user_role: "owner" | "admin" | "manager" | "staff" | null;
};
