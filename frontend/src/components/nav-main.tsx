import {
  SidebarGroup,
  SidebarGroupContent,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "~/components/ui/sidebar";
import {
  CalendarDays,
  Car,
  LayoutDashboard,
  UsersRound,
  Warehouse,
} from "lucide-react";
import Link from "next/link";
import { useParams, usePathname } from "next/navigation";

const menuItems = (org_id: string) => [
  {
    title: "Обзор",
    link: `/dashboard/org/${org_id}`,
    icon: LayoutDashboard,
    exact: true,
  },
  {
    title: "Записи",
    link: `/dashboard/org/${org_id}/appointments`,
    icon: CalendarDays,
    exact: true,
  },
  {
    title: "Клиенты",
    link: `/dashboard/org/${org_id}/clients`,
    icon: UsersRound,
    exact: true,
  },
  {
    title: "Автомобили",
    link: `/dashboard/org/${org_id}/cars`,
    icon: Car,
    exact: true,
  },
  {
    title: "Склад",
    link: `/dashboard/org/${org_id}/warehouse`,
    icon: Warehouse,
    exact: true,
  },
];
export function NavMain() {
  const pathname = usePathname();
  const params = useParams();
  const org_id = params.org_id as string;

  const isActive = (href: string, exact?: boolean) => {
    if (exact) {
      return href === pathname;
    }
    return pathname.startsWith(href);
  };

  return (
    <SidebarGroup>
      <SidebarGroupContent>
        <SidebarMenu>
          {menuItems(org_id).map((item) => (
            <SidebarMenuItem key={item.title}>
              <SidebarMenuButton
                asChild
                isActive={isActive(item.link, item.exact)}
              >
                <Link href={item.link}>
                  {item.icon && <item.icon />}
                  <span>{item.title}</span>
                </Link>
              </SidebarMenuButton>
            </SidebarMenuItem>
          ))}
        </SidebarMenu>
      </SidebarGroupContent>
    </SidebarGroup>
  );
}
