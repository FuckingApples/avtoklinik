import api from "~/lib/axios";
import type {
  Color,
  RegistriesCounts,
} from "~/types/registries";
import type { ApiResponse } from "~/types/api";


export async function getColors(orgId: number) {
  return api.get<Color[]>(`/v1/organizations/${orgId}/registries/colors/`).then((res) => res.data);
}

export async function getRegistry<Registry, Filter>(registry: string, orgId: number, filters?: Filter) {
  const params = new URLSearchParams();

  if (filters) {
    Object.entries(filters).forEach(([key, value]) => {
      if (value !== undefined && value !== null) {
        params.append(key, value.toString());
      }
    });
  }

  return api
      .get<ApiResponse<Registry>>(`/v1/organizations/${orgId}/registries/${registry}/`, { params })
      .then((res) => res.data);
}

export async function getRegistriesCounts(orgId: number): Promise<RegistriesCounts> {
  return api
    .get<RegistriesCounts>(`/v1/organizations/${orgId}/registries/counts/`)
    .then((res) => res.data);
}
