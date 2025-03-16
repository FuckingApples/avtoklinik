"use client";

import { DashboardSidebar } from "~/components/dashboard-sidebar";
import { SidebarInset, SidebarProvider } from "~/components/ui/sidebar";
import React, { useEffect, useState } from "react";
import { useUser } from "~/hooks/use-user";
import { useParams } from "next/navigation";
import Error from "next/error";

export default function DashboardClientLayout({
  children,
  defaultOpen,
}: React.PropsWithChildren<{
  defaultOpen: boolean;
}>) {
  const { data: user, isLoading } = useUser();
  const { org_id } = useParams();
  const [hasAccess, setHasAccess] = useState<boolean | null>(null);

  useEffect(() => {
    if (!isLoading && user) {
      setHasAccess(user.organizations.some((org) => org.public_id === org_id));
    }
  }, [user, isLoading, org_id]);

  if (hasAccess === false) return <Error statusCode={404} />;

  return (
    <SidebarProvider defaultOpen={defaultOpen}>
      <DashboardSidebar />
      <SidebarInset>{children}</SidebarInset>
    </SidebarProvider>
  );
}
