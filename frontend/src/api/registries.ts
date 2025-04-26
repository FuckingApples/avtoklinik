import api from "~/lib/axios";
import type {
  Color,
  Country,
  RegistriesCounts,
} from "~/types/registries";
import { getNumericOrgId } from "~/api/organization";

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

export async function getCountries(): Promise<Country[]> {
  return Promise.resolve(COUNTRIES);
}

export function getCountryName(countryCode: string): string {
  const country = COUNTRIES.find(c => c.code === countryCode);
  return country ? country.name : countryCode;
}

export async function getRegistriesCounts(orgId: string): Promise<RegistriesCounts> {
  const numericOrgId = await getNumericOrgId(orgId);
  return api
    .get<RegistriesCounts>(`/v1/organizations/${numericOrgId}/registries/counts/`)
    .then((res) => res.data);
}
