import React from "react";
import { cookies } from "next/headers";
import ProtectedRoute from "~/components/protected-route";
import DashboardClientLayout from "~/app/dashboard/org/[org_id]/client-layout";

export default async function DashboardLayout({
  children,
}: Readonly<React.PropsWithChildren>) {
  const cookieStore = await cookies();
  const defaultOpen = cookieStore.get("sidebar_state")?.value === "true";

  return (
    <ProtectedRoute>
      <DashboardClientLayout defaultOpen={defaultOpen}>
        {children}
      </DashboardClientLayout>
    </ProtectedRoute>
  );
}
