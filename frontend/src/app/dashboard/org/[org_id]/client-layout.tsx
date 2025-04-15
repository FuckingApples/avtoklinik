"use client";

import { DashboardSidebar } from "~/components/dashboard-sidebar";
import { SidebarInset, SidebarProvider } from "~/components/ui/sidebar";
import React, { useMemo } from "react";
import { useUser } from "~/hooks/use-user";
import { useParams } from "next/navigation";
import Error from "next/error";
import { useOrganization } from "~/hooks/use-organization";

export default function DashboardClientLayout({
  children,
  defaultOpen,
}: React.PropsWithChildren<{
  defaultOpen: boolean;
}>) {
  const { data: user, isLoading: isUserLoading } = useUser();
  const { org_id } = useParams();

  const hasAccess = useMemo(() => {
    return (
      !isUserLoading &&
      user?.organizations.some((org) => org.public_id === org_id)
    );
  }, [isUserLoading, org_id, user?.organizations]);

  const organizationId = useMemo(() => {
    return (
      user?.organizations.find((org) => org.public_id === org_id)?.id ?? null
    );
  }, [user, org_id]);

  useOrganization({
    id: organizationId,
    enabled: hasAccess && !!organizationId,
  });

  if (hasAccess === false) return <Error statusCode={404} />;

  return (
    <SidebarProvider defaultOpen={defaultOpen}>
      <DashboardSidebar />
      <SidebarInset>{children}</SidebarInset>
    </SidebarProvider>
  );
}
