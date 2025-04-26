import {
  LucideIcon,
  Folder,
  Tag,
  Ruler,
  Palette,
  Car,
  Building,
  Timer,
} from "lucide-react";

export interface RegistryItem {
  title: string;
  path: string;
  href: (org_id: string) => string;
  count: number;
  icon: LucideIcon;
  addButtonText: string;
  importEnabled?: boolean;
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
        path: "categories",
        href: (org_id) => `/dashboard/org/${org_id}/registries/categories`,
        count: 12,
        icon: Folder,
        addButtonText: "Добавить категорию",
        importEnabled: true,
      },
      {
        title: "Производители",
        path: "manufacturers",
        href: (org_id) => `/dashboard/org/${org_id}/registries/manufacturers`,
        count: 28,
        icon: Tag,
        addButtonText: "Добавить производителя",
        importEnabled: true,
      },
      {
        title: "Единицы измерения",
        path: "measurement-units",
        href: (org_id) => `/dashboard/org/${org_id}/registries/measurement-units`,
        count: 8,
        icon: Ruler,
        addButtonText: "Добавить единицу измерения",
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
        addButtonText: "Добавить цвет",
        importEnabled: true,
      },
      {
        title: "Комплектность",
        path: "equipments",
        href: (org_id) => `/dashboard/org/${org_id}/registries/equipments`,
        count: 12,
        icon: Car,
        addButtonText: "Добавить комплектность",
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
        addButtonText: "Добавить рабочее место",
        importEnabled: true,
      },
      {
        title: "Стоимость нормо-часа",
        path: "hourly-wages",
        href: (org_id) => `/dashboard/org/${org_id}/registries/hourly-wages`,
        count: 14,
        icon: Timer,
        addButtonText: "Добавить стоимость",
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