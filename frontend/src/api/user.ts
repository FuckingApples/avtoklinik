import api from "~/lib/axios";
import type { User } from "~/types/user";

export async function getUserInfo() {
  return api.get<User>("/v1/user").then((res) => res.data);
}
