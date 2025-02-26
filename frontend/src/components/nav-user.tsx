"use client";

import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "~/components/ui/sidebar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "~/components/ui/avatar";
import {
  Bell,
  ChevronsUpDown,
  Gem,
  LogOut,
  Settings,
  User,
} from "lucide-react";
import { useAuthStore } from "~/store/auth";
import { logoutUser } from "~/api/auth";
import { GlowEffect } from "~/components/ui/glow-effect";

type NavUserProps = {
  first_name: string | undefined;
  last_name: string | undefined;
  email: string | undefined;
};

export function NavUser({ first_name, last_name, email }: NavUserProps) {
  const { isMobile } = useSidebar();
  const { logout } = useAuthStore();

  const onLogoutClick = async () => {
    await logoutUser();
    logout();
  };

  return (
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <SidebarMenuButton
              size="lg"
              className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
            >
              <Avatar className="h-8 w-8 rounded-lg">
                <AvatarImage />
                <AvatarFallback className="rounded-lg">
                  {first_name?.charAt(0)}
                  {last_name?.charAt(0)}
                </AvatarFallback>
              </Avatar>
              <div className="grid flex-1 text-left text-sm leading-tight">
                <span className="truncate font-semibold">
                  {first_name} {last_name}
                </span>
                <span className="truncate text-xs">{email}</span>
              </div>
              <ChevronsUpDown className="ml-auto size-4" />
            </SidebarMenuButton>
          </DropdownMenuTrigger>
          <DropdownMenuContent
            className="w-(--radix-dropdown-menu-trigger-width) min-w-56 rounded-lg"
            side={isMobile ? "bottom" : "right"}
            align="end"
            sideOffset={4}
          >
            <DropdownMenuGroup>
              <DropdownMenuItem className="bg-background">
                <Gem />
                Изменить тариф
              </DropdownMenuItem>
            </DropdownMenuGroup>
            <DropdownMenuSeparator />
            <DropdownMenuGroup>
              <DropdownMenuItem>
                <User />
                Профиль
              </DropdownMenuItem>
              <DropdownMenuItem>
                <Bell />
                Уведомления
              </DropdownMenuItem>
              <DropdownMenuItem>
                <Settings />
                Настройки
              </DropdownMenuItem>
            </DropdownMenuGroup>
            <DropdownMenuSeparator />
            <DropdownMenuItem variant="destructive" onClick={onLogoutClick}>
              <LogOut />
              Выйти
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </SidebarMenuItem>
    </SidebarMenu>
  );
}
