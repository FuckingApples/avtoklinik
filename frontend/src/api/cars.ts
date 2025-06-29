import api from "~/lib/axios";
import type { Car } from "~/types/car";
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

export async function getCar(orgId: number, carId: string) {
  return api
    .get<Car>(`/v1/organizations/${orgId}/cars/${carId}/`)
    .then((res) => res.data);
}

export async function createCar(
  orgId: number,
  data: Partial<Car> & { client_id?: string },
) {
  return api
    .post<Car>(`/v1/organizations/${orgId}/cars/`, data)
    .then((res) => res.data);
}

export async function updateCar(
  orgId: number,
  carId: string,
  data: Partial<Car> & { client_id?: string },
) {
  return api
    .patch<Car>(`/v1/organizations/${orgId}/cars/${carId}/`, data)
    .then((res) => res.data);
}

export async function deleteCar(orgId: number, carId: string) {
  return api.delete(`/v1/organizations/${orgId}/cars/${carId}/`);
}
