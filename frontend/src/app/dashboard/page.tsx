"use client";

import { useUser } from "~/hooks/use-user";
import { useRouter } from "next/navigation";
import React, { useEffect } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import { Button } from "~/components/ui/button";

export default function DashboardPage() {
  const { data: user, isLoading } = useUser();
  const router = useRouter();

  useEffect(() => {
    if (!isLoading) {
      if (user?.organizations.length === 0) {
        router.replace("/dashboard/new?first");
      }
    }
  }, [user, isLoading, router]);

  const selectOrganization = (org_id: string) => {
    router.push(`/dashboard/org/${org_id}`);
  };

  return (
    <div className="flex min-h-screen items-center justify-center">
      <Card className="flex h-screen min-w-[350px] justify-center sm:h-fit sm:w-[500px]">
        <CardHeader>
          <CardTitle>С возвращением, {user?.first_name}!</CardTitle>
          <CardDescription>Ваши организации</CardDescription>
        </CardHeader>
        <CardContent className="flex flex-col gap-2">
          {user?.organizations.map((organization) => (
            <Card
              key={organization.public_id}
              className="hover:bg-accent/50 cursor-pointer transition-all"
              onClick={() => selectOrganization(organization.public_id)}
            >
              <CardHeader className="flex flex-row items-center gap-3">
                <div className="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-10 items-center justify-center rounded-lg">
                  ТО
                </div>
                <div className="flex flex-col justify-center gap-0.5">
                  <CardTitle className="line-clamp-2">
                    {organization.name}
                  </CardTitle>
                  <CardDescription>{organization.user_role}</CardDescription>
                </div>
              </CardHeader>
            </Card>
          ))}
        </CardContent>
        <CardFooter>
          <Button
            className="w-full"
            size="lg"
            onClick={() => {
              router.push(`/dashboard/new`);
            }}
          >
            Добавить новую организацию
          </Button>
        </CardFooter>
      </Card>
    </div>
  );
}
