"use client";

import { cn, generateSmoothGradient, getInitials } from "~/lib/utils";
import { useUserStore } from "~/store/user";
import { Skeleton } from "~/components/ui/skeleton";
import { Avatar, AvatarFallback, AvatarImage } from "~/components/ui/avatar";
import React from "react";
import { Button } from "~/components/ui/button";
import { SaveIcon, XIcon } from "lucide-react";
import { Separator } from "~/components/ui/separator";

type UserInfoBannerProps = React.ComponentProps<"section"> & {
  isDirty: boolean;
  onClear: React.MouseEventHandler<HTMLButtonElement>;
};

export default function UserInfoBanner({
  className,
  isDirty,
  onClear,
  ...props
}: UserInfoBannerProps) {
  const { user } = useUserStore();

  return (
    <section
      className={cn("px-3 lg:mx-auto lg:max-w-5xl", className)}
      {...props}
    >
      <span className="hidden xl:block">TEST</span>
      {user ? (
        <div
          className="animate-user-banner-gradient aspect-4/1 rounded-lg bg-[length:400%_400%] sm:aspect-5/1 lg:aspect-6/1"
          style={{
            backgroundImage: generateSmoothGradient(
              `${user?.first_name} ${user?.last_name}`,
            ),
          }}
        />
      ) : (
        <Skeleton className="aspect-4/1 rounded-lg sm:aspect-6/1 lg:aspect-7/1" />
      )}
      <div className="relative mt-3 flex items-center justify-between">
        <Avatar className="absolute top-0 ml-3 size-20 -translate-y-1/2 rounded-xl lg:ml-6 lg:size-25">
          <AvatarImage src={user?.avatar} />
          <AvatarFallback className="rounded-xl text-3xl">
            {getInitials(`${user?.first_name} ${user?.last_name} `)}
          </AvatarFallback>
        </Avatar>
        <div className="text-foreground ml-26 flex flex-col truncate text-sm md:text-base lg:ml-36 lg:text-xl">
          <span className="truncate font-semibold">
            {user?.first_name} {user?.last_name}
          </span>
          <span className="text-muted-foreground truncate text-xs md:text-sm">
            {user?.email}
          </span>
        </div>
        <div className="ml-3 flex gap-3">
          <Button variant="outline" disabled={!isDirty} onClick={onClear}>
            <XIcon />
            <span className="hidden sm:block">Отменить</span>
          </Button>
          <Button form="user-settings" type="submit" disabled={!isDirty}>
            <SaveIcon />
            <span className="hidden sm:block">Сохранить</span>
          </Button>
        </div>
      </div>
      <Separator className="my-4 max-w-5xl" />
    </section>
  );
}
