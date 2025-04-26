import api from "~/lib/axios";
import type { Car } from "~/types/car";
import { getNumericOrgId } from "~/api/organization";
import type { GetCarsFilters } from "~/store/cars";
import type { ApiResponse } from "~/types/api";

export async function getCars(orgId: number, filters?: GetCarsFilters) {
  const params = new URLSearchParams();

  if (filters) {
    Object.entries(filters).forEach(([key, value]) => {
      if (value !== undefined && value !== null) {
        params.append(key, value.toString());
      }
    });
  }

  return api
    .get<ApiResponse<Car>>(`/v1/organizations/${orgId}/cars/`, { params })
    .then((res) => res.data);
}

export async function getCar(orgId: string, carId: string) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api
    .get<Car>(`/v1/organizations/${numericOrgId}/cars/${carId}/`)
    .then((res) => res.data);
}

export async function createCar(
  orgId: string,
  data: Partial<Car> & { client_id?: string },
) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api
    .post<Car>(`/v1/organizations/${numericOrgId}/cars/`, data)
    .then((res) => res.data);
}

export async function updateCar(
  orgId: string,
  carId: string,
  data: Partial<Car> & { client_id?: string },
) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api
    .patch<Car>(`/v1/organizations/${numericOrgId}/cars/${carId}/`, data)
    .then((res) => res.data);
}

export async function deleteCar(orgId: string, carId: string) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api.delete(`/v1/organizations/${numericOrgId}/cars/${carId}/`);
}
