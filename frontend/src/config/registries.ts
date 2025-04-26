import {
  Folder,
  Tag,
  Ruler,
  Palette,
  Car,
  Building,
  Timer,
} from "lucide-react";
import type { RegistrySection } from "~/types/registries";

export const registriesSections: RegistrySection[] = [
  {
    title: "Основные",
    items: [
      {
        title: "Категории",
        path: "categories",
        href: (org_id) => `/dashboard/org/${org_id}/registries/categories`,
        count: 12,
        icon: Folder,
        buttonTitle: "Добавить категорию",
        importEnabled: true,
      },
      {
        title: "Производители",
        path: "manufacturers",
        href: (org_id) => `/dashboard/org/${org_id}/registries/manufacturers`,
        count: 28,
        icon: Tag,
        buttonTitle: "Добавить производителя",
        importEnabled: true,
      },
      {
        title: "Единицы измерения",
        path: "measurement-units",
        href: (org_id) => `/dashboard/org/${org_id}/registries/measurement-units`,
        count: 8,
        icon: Ruler,
        buttonTitle: "Добавить единицу измерения",
        importEnabled: true,
      },
    ],
  },
  {
    title: "Автомобиль",
    items: [
      {
        title: "Цвета",
        path: "colors",
        href: (org_id) => `/dashboard/org/${org_id}/registries/colors`,
        count: 15,
        icon: Palette,
        buttonTitle: "Добавить цвет",
        importEnabled: true,
      },
      {
        title: "Комплектность",
        path: "equipments",
        href: (org_id) => `/dashboard/org/${org_id}/registries/equipments`,
        count: 12,
        icon: Car,
        buttonTitle: "Добавить комплектность",
        importEnabled: true,
      },
    ],
  },
  {
    title: "Организация",
    items: [
      {
        title: "Рабочие места",
        path: "workplaces",
        href: (org_id) => `/dashboard/org/${org_id}/registries/workplaces`,
        count: 20,
        icon: Building,
        buttonTitle: "Добавить рабочее место",
        importEnabled: true,
      },
      {
        title: "Стоимость нормо-часа",
        path: "hourly-wages",
        href: (org_id) => `/dashboard/org/${org_id}/registries/hourly-wages`,
        count: 14,
        icon: Timer,
        buttonTitle: "Добавить стоимость",
        importEnabled: true,
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

export function getCurrentRegistry(pathname: string, org_id: string) {
  const lastPathSegment = pathname.split('/').pop() ?? '';

  for (const section of registriesSections) {
    const item = section.items.find(item => item.path === lastPathSegment);
    if (item) {
      return {
        ...item,
        href: item.href(org_id),
        section: section.title
      };
    }
  }
  return null;
} 