"use client";

import { NavRegistries } from "~/components/nav-registries";
import DashboardHeader from "~/components/ui/dashboard-header";
import {
  ChevronDownIcon,
  ChevronRight,
  FileUpIcon,
  PlusIcon,
} from "lucide-react";
import { Button } from "~/components/ui/button";
import { ButtonsGroup } from "~/components/ui/buttons-group";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import { getCurrentRegistry } from "~/config/registries-content";
import Link from "next/link";
import React from "react";
import { usePathname, useParams } from "next/navigation";

export default function RegistriesLayout({
  children,
}: Readonly<React.PropsWithChildren>) {
  const pathname = usePathname();
  const params = useParams();
  const org_id = params.org_id as string;

  const mainPage = `/dashboard/org/${org_id}/registries`;
  const isMainPage = pathname === mainPage;
  const registry = getCurrentRegistry(pathname, org_id);
  const showAddButton = !isMainPage && !!registry;

  return (
    <div className="flex h-full flex-col">
      <DashboardHeader>
        <DashboardHeader.Title>
          {!isMainPage && registry ? (
            <div className="flex items-center gap-2">
              <Link
                href={mainPage}
                className="transition-colors hover:text-gray-800"
              >
                <span>Справочники</span>
              </Link>
              <ChevronRight className="text-muted-foreground h-4 w-4" />
              <div className="flex h-8 w-8 items-center justify-center rounded-lg border border-blue-100 bg-gradient-to-br from-blue-50 to-blue-100 shadow-sm">
                {registry.icon && (
                  <registry.icon
                    className="h-5 w-5 text-blue-500"
                    strokeWidth={2.2}
                  />
                )}
              </div>
              <span>{registry.title}</span>
            </div>
          ) : (
            "Справочники"
          )}
        </DashboardHeader.Title>

        {showAddButton && (
          <DashboardHeader.ActionButton asChild>
            <ButtonsGroup>
              <Button>
                <PlusIcon />
                <span className="hidden sm:block">{registry?.buttonTitle}</span>
              </Button>
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button size="sm" className="rounded-l-none">
                    <ChevronDownIcon />
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end" sideOffset={4}>
                  <DropdownMenuItem>
                    <FileUpIcon />
                    Экспортировать из файла
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </ButtonsGroup>
          </DashboardHeader.ActionButton>
        )}
      </DashboardHeader>

      <div className="flex flex-1">
        <NavRegistries />
        {children}
      </div>
    </div>
  );
}
