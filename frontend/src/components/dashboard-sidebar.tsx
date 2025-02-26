"use client";

import React from "react";
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
} from "~/components/ui/sidebar";
import { OrganizationSwitcher } from "~/components/organization-switcher";
import { NavUser } from "~/components/nav-user";
import { useQuery } from "@tanstack/react-query";
import { getUserInfo } from "~/api/user";
import { Skeleton } from "~/components/ui/skeleton";

export function DashboardSidebar({
  ...props
}: React.ComponentProps<typeof Sidebar>) {
  const { data: user, isLoading } = useQuery({
    queryKey: ["user"],
    queryFn: getUserInfo,
    staleTime: 1000 * 60 * 5,
  });

  return (
    <Sidebar variant="inset" collapsible="icon" {...props}>
      <SidebarHeader>
        {!isLoading ? (
          <OrganizationSwitcher organizations={user?.organizations} />
        ) : (
          <Skeleton className="h-12 w-full" />
        )}
      </SidebarHeader>
      <SidebarContent></SidebarContent>
      <SidebarFooter>
        {!isLoading ? (
          <NavUser
            first_name={user?.first_name}
            last_name={user?.last_name}
            email={user?.email}
          />
        ) : (
          <Skeleton className="h-12 w-full" />
        )}
      </SidebarFooter>
    </Sidebar>
  );
}
