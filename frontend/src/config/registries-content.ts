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
        icon: Folder,
        buttonTitle: "Добавить категорию",
        importEnabled: true,
      },
      {
        title: "Производители",
        path: "manufacturers",
        href: (org_id) => `/dashboard/org/${org_id}/registries/manufacturers`,
        icon: Tag,
        buttonTitle: "Добавить производителя",
        importEnabled: true,
      },
      {
        title: "Единицы измерения",
        path: "measurement-units",
        href: (org_id) =>
          `/dashboard/org/${org_id}/registries/measurement-units`,
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
        icon: Palette,
        buttonTitle: "Добавить цвет",
        importEnabled: true,
      },
      {
        title: "Комплектности",
        path: "equipments",
        href: (org_id) => `/dashboard/org/${org_id}/registries/equipments`,
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
        icon: Building,
        buttonTitle: "Добавить рабочее место",
        importEnabled: true,
      },
      {
        title: "Нормо-часы",
        path: "hourly-wages",
        href: (org_id) => `/dashboard/org/${org_id}/registries/hourly-wages`,
        icon: Timer,
        buttonTitle: "Добавить стоимость",
        importEnabled: true,
      },
    ],
  },
];

export function getRegistriesData(orgId: string) {
  return registriesSections.map((section) => ({
    ...section,
    items: section.items.map((item) => ({
      ...item,
      href: item.href(orgId),
    })),
  }));
}

export function getCurrentRegistry(pathname: string, org_id: string) {
  const lastPathSegment = pathname.split("/").pop() ?? "";

  for (const section of registriesSections) {
    const item = section.items.find((item) => item.path === lastPathSegment);
    if (item) {
      return {
        ...item,
        href: item.href(org_id),
        section: section.title,
      };
    }
  }
  return null;
}
