import api from "~/lib/axios";
import { Color } from "~/types/car";
import { getNumericOrgId } from "~/api/organization";

export interface Country {
  code: string;
  name: string;
}

export const COUNTRIES: Country[] = [
  { code: "RU", name: "Россия" },
  { code: "BY", name: "Беларусь" },
  { code: "KZ", name: "Казахстан" },
  { code: "UA", name: "Украина" },
  { code: "AM", name: "Армения" },
  { code: "GE", name: "Грузия" },
  { code: "AZ", name: "Азербайджан" },
  { code: "LT", name: "Литва" },
  { code: "LV", name: "Латвия" },
  { code: "EE", name: "Эстония" },
  { code: "MD", name: "Молдова" },
  { code: "TJ", name: "Таджикистан" },
  { code: "TM", name: "Туркменистан" },
  { code: "UZ", name: "Узбекистан" },
  { code: "KG", name: "Кыргызстан" },
  { code: "DE", name: "Германия" },
  { code: "FR", name: "Франция" },
  { code: "ES", name: "Испания" },
  { code: "IT", name: "Италия" },
  { code: "GB", name: "Великобритания" },
  { code: "PL", name: "Польша" },
  { code: "CZ", name: "Чехия" },
  { code: "SK", name: "Словакия" },
  { code: "HU", name: "Венгрия" },
  { code: "RO", name: "Румыния" },
  { code: "BG", name: "Болгария" },
  { code: "TR", name: "Турция" }
];

export async function getColors(orgId: string) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api.get<Color[]>(`/v1/organizations/${numericOrgId}/registries/colors/`).then((res) => res.data);
}

export async function getColor(orgId: string, colorId: string) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api.get<Color>(`/v1/organizations/${numericOrgId}/registries/colors/${colorId}/`).then((res) => res.data);
}

export async function getCountries(): Promise<Country[]> {
  return Promise.resolve(COUNTRIES);
}

export function getCountryName(countryCode: string): string {
  const country = COUNTRIES.find(c => c.code === countryCode);
  return country ? country.name : countryCode;
}

export async function createColor(orgId: string, data: Partial<Color>) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api.post<Color>(`/v1/organizations/${numericOrgId}/registries/colors/`, data).then((res) => res.data);
}

export async function deleteColor(orgId: string, colorId: string) {
  const numericOrgId = await getNumericOrgId(orgId);
  return api.delete(`/v1/organizations/${numericOrgId}/registries/colors/${colorId}/`);
} 