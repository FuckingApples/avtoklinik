export interface RegistryItem {
  title: string;
  href: (org_id: string) => string;
  count: number;
}

export interface RegistrySection {
  title: string;
  items: RegistryItem[];
}

export const registriesSections: RegistrySection[] = [
  {
    title: "Основные",
    items: [
      {
        title: "Категории",
        href: (org_id) => `/dashboard/org/${org_id}/registries/categories`,
        count: 12,
      },
      {
        title: "Производители",
        href: (org_id) => `/dashboard/org/${org_id}/registries/manufacturers`,
        count: 28,
      },
      {
        title: "Единицы измерения",
        href: (org_id) => `/dashboard/org/${org_id}/registries/measurement-units`,
        count: 8,
      },
    ],
  },
  {
    title: "Автомобиль",
    items: [
      {
        title: "Цвета",
        href: (org_id) => `/dashboard/org/${org_id}/registries/colors`,
        count: 15,
      },
    ],
  },
  {
    title: "Организация",
    items: [
      {
        title: "Рабочие места",
        href: (org_id) => `/dashboard/org/${org_id}/registries/workplaces`,
        count: 20,
      },
    ],
  },
];

export function getRegistriesData(orgId: string) {
  return registriesSections.map(section => ({
    ...section,
    items: section.items.map(item => ({
      ...item,
      href: item.href(orgId),
    }))
  }));
} 