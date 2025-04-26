import React from "react";
import { RegistriesNavigation } from "~/components/registries-navigation";
import DashboardHeader from "~/components/ui/dashboard-header";

export default function RegistriesLayout({
  children,
}: Readonly<React.PropsWithChildren>) {
  return (
    <div className="flex h-full flex-col">
      <DashboardHeader>
        <DashboardHeader.Title>Справочники</DashboardHeader.Title>
      </DashboardHeader>

      <div className="flex flex-1">
        <RegistriesNavigation />
          {children}
      </div>
    </div>
  );
} 