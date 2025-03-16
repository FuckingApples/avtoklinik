"use client";

import { cn, generateSmoothGradient, getInitials } from "~/lib/utils";
import { useUserStore } from "~/store/user";
import { Skeleton } from "~/components/ui/skeleton";
import { Avatar, AvatarFallback, AvatarImage } from "~/components/ui/avatar";
import React from "react";
import { Button } from "~/components/ui/button";
import { Save } from "lucide-react";

export default function UserInfoBanner({
  className,
  ...props
}: React.ComponentProps<"section">) {
  const { user } = useUserStore();

  return (
    <section className={cn("mx-3", className)} {...props}>
      {user ? (
        <div
          className="animate-user-banner-gradient aspect-4/1 rounded-lg bg-[length:400%_400%]"
          style={{
            backgroundImage: generateSmoothGradient(
              `${user?.first_name} ${user?.last_name}`,
            ),
          }}
        />
      ) : (
        <Skeleton className="aspect-4/1 rounded-lg" />
      )}
      <div className="relative mt-3 flex justify-between">
        <Avatar className="absolute top-0 ml-3 size-20 -translate-y-1/2 rounded-xl">
          <AvatarImage src={user?.avatar} />
          <AvatarFallback className="rounded-xl text-3xl">
            {getInitials(`${user?.first_name} ${user?.last_name} `)}
          </AvatarFallback>
        </Avatar>
        <div className="text-foreground ml-26 flex flex-col text-sm">
          <span>
            {user?.first_name} {user?.last_name}
          </span>
          <span className="text-muted-foreground text-xs">{user?.email}</span>
        </div>
        <Button form="user-settings" type="submit" size="icon">
          <Save />
        </Button>
      </div>
    </section>
  );
}
