import DashboardHeader from "~/components/ui/dashboard-header";
import { HelpMenu } from "~/components/help-menu";

export default function OrganizationDashboardPage() {
  return (
    <div>
      <DashboardHeader>
        <DashboardHeader.Title>Главная</DashboardHeader.Title>
      </DashboardHeader>
      <HelpMenu pageKey="main" />
    </div>
  );
}
