import React from "react";
import { DashboardSidebar } from "~/components/dashboard-sidebar";
import { SidebarInset, SidebarProvider } from "~/components/ui/sidebar";
import { cookies } from "next/headers";
import ProtectedRoute from "~/components/protected-route";

export default async function DashboardLayout({
  children,
}: Readonly<React.PropsWithChildren>) {
  const cookieStore = await cookies();
  const defaultOpen = cookieStore.get("sidebar_state")?.value === "true";

  return (
    <ProtectedRoute>
      <SidebarProvider defaultOpen={defaultOpen}>
        <DashboardSidebar />
        <SidebarInset>{children}</SidebarInset>
      </SidebarProvider>
    </ProtectedRoute>
  );
}
