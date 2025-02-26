"use client";

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "~/components/ui/sidebar";
import React from "react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import { ChevronsUpDown, Plus } from "lucide-react";
import type { GetOrganizationInfo } from "~/api/user";
import { cn } from "~/lib/utils";
import { useParams, useRouter } from "next/navigation";

export function OrganizationSwitcher({
  organizations,
}: {
  organizations: GetOrganizationInfo[] | undefined;
}) {
  const { isMobile } = useSidebar();
  const router = useRouter();
  const { organization_id } = useParams<{ organization_id: string }>();

  return (
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton
              size="lg"
              className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
            >
              <div className="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg">
                ТО
              </div>
              <div className="grid flex-1 text-left text-sm leading-tight">
                <span className="truncate font-semibold">
                  {
                    organizations?.find((organization) => {
                      console.log(organization.public_id, organization_id);
                      return organization.public_id === organization_id;
                    })?.name
                  }
                </span>
                <span className="truncate text-xs">Бесплатный</span>
              </div>
              <ChevronsUpDown className="ml-auto" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            className="w-(--radix-dropdown-menu-trigger-width) min-w-56 rounded-lg"
            align="start"
            side={isMobile ? "bottom" : "right"}
            sideOffset={4}
          >
            <DropdownMenuLabel className="text-muted-foreground text-xs">
              Организации
            </DropdownMenuLabel>
            {organizations?.map((organization) => (
              <DropdownMenuItem
                key={organization.public_id}
                onClick={() =>
                  router.push(`/dashboard/${organization.public_id}`)
                }
                className={cn(
                  "gap-2 truncate p-2",
                  organization.public_id === organization_id
                    ? "bg-accent"
                    : null,
                )}
              >
                <div className="flex size-6 items-center justify-center rounded-sm border">
                  TO
                </div>
                {organization.name}
              </DropdownMenuItem>
            ))}
            <DropdownMenuSeparator />
            <DropdownMenuItem
              className="gap-2 p-2"
              onClick={() => router.push("/dashboard/create")}
            >
              <div className="bg-background flex size-6 items-center justify-center rounded-md border">
                <Plus className="size-4" />
              </div>
              <div className="text-muted-foreground font-medium">
                Добавить организацию
              </div>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  );
}
