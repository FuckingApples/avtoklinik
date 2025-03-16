"use client";
import React from "react";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "~/components/ui/sheet";
import { useIsMobile } from "~/hooks/use-mobile";
import { cn } from "~/lib/utils";
import { ChevronsUpDown, LogOut, Menu } from "lucide-react";
import { Button } from "~/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "~/components/ui/avatar";
import { Skeleton } from "~/components/ui/skeleton";
import { useUser } from "~/hooks/use-user";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import { logoutUser } from "~/api/auth";
import { useAuthStore } from "~/store/auth";

const SIDEBAR_WIDTH_MOBILE = "18rem";

export default function UserSpaceNav({
  side = "left",
  className,
  children,
}: React.ComponentProps<"div"> & {
  side?: "left" | "right";
}) {
  const isMobile = useIsMobile();
  const { logout } = useAuthStore();
  const { data: user } = useUser();

  const onLogoutClick = async () => {
    await logoutUser();
    logout();
  };

  if (isMobile) {
    return (
      <Sheet>
        <SheetTrigger asChild>
          <Button
            variant="ghost"
            size="icon"
            className={cn("h-7 w-7", className)}
          >
            <Menu />
            <span className="sr-only">Toggle menu</span>
          </Button>
        </SheetTrigger>
        <SheetContent
          data-mobile="true"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
            } as React.CSSProperties
          }
          side={side}
        >
          <SheetHeader className="sr-only">
            <SheetTitle>Menu</SheetTitle>
            <SheetDescription>Displays the mobile menu.</SheetDescription>
          </SheetHeader>
          {children}
          <SheetFooter>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <div className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground flex flex-row items-center gap-2 rounded-md p-2">
                  <Avatar className="size-8 rounded-lg">
                    <AvatarImage src={user?.avatar} />
                    <AvatarFallback className="rounded-lg">
                      {user?.first_name.charAt(0)}
                      {user?.last_name.charAt(0)}
                    </AvatarFallback>
                  </Avatar>
                  <div className="grid flex-1 text-left text-sm leading-tight">
                    {user ? (
                      <>
                        <span className="truncate font-semibold">
                          {user?.first_name} {user?.last_name}
                        </span>
                        <span className="truncate text-xs">{user?.email}</span>
                      </>
                    ) : (
                      <div className="flex flex-col gap-0.5">
                        <Skeleton className="h-3 rounded-xs" />
                        <Skeleton className="h-3 w-1/2 rounded-xs" />
                      </div>
                    )}
                  </div>
                  <ChevronsUpDown className="ml-auto size-4" />
                </div>
              </DropdownMenuTrigger>
              <DropdownMenuContent
                side="top"
                align="end"
                className="w-(--radix-dropdown-menu-trigger-width) min-w-56 rounded-lg"
                sideOffset={4}
              >
                <DropdownMenuItem variant="destructive" onClick={onLogoutClick}>
                  <LogOut />
                  Выйти
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    );
  }
}
