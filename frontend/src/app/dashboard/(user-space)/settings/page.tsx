"use client";

import { Tabs, TabsContent, TabsList, TabsTrigger } from "~/components/ui/tabs";
import { ScrollArea, ScrollBar } from "~/components/ui/scroll-area";
import UserInfoBanner from "~/components/user-info-banner";
import { useQueryState } from "nuqs";
import DetailsTab from "~/app/dashboard/(user-space)/settings/details";
import { useForm } from "react-hook-form";
import { useUserStore } from "~/store/user";
import {
  type TUserSettingsSchema,
  userSettingsSchema,
} from "~/utils/validation/user-settings";
import { zodResolver } from "@hookform/resolvers/zod";
import { useEffect, useState } from "react";

export default function ProfilePage() {
  const [page, setPage] = useQueryState("page", { defaultValue: "details" });
  const [dataLoaded, setDataLoaded] = useState(false);

  const { user } = useUserStore();
  const form = useForm<TUserSettingsSchema>({
    defaultValues: {
      first_name: "",
      last_name: "",
      email: "",
    },
    resolver: zodResolver(userSettingsSchema),
  });

  useEffect(() => {
    if (user && !dataLoaded) {
      form.reset({
        first_name: user?.first_name,
        last_name: user?.last_name,
        email: user?.email,
      });
      setDataLoaded(true);
    }
  }, [user, form, dataLoaded]);

  return (
    <>
      <UserInfoBanner className="mt-3 mb-6" />
      <section className="flex flex-col">
        <div className="mx-3">
          <h3 className="text-foreground text-2xl leading-none font-bold">
            Настройки
          </h3>
          <span className="text-muted-foreground text-sm">
            Настройте свой профиль
          </span>
        </div>
        <Tabs
          defaultValue={page}
          onValueChange={setPage}
          className="overflow-visible"
        >
          <ScrollArea>
            <TabsList className="m-3">
              <TabsTrigger value="details">Мои данные</TabsTrigger>
              <TabsTrigger value="security">Безопасность</TabsTrigger>
              <TabsTrigger value="apperance">Внешний вид</TabsTrigger>
              <TabsTrigger value="notifications">Уведомления</TabsTrigger>
            </TabsList>
            <ScrollBar orientation="horizontal" className="hidden" />
          </ScrollArea>
          <TabsContent value="details">
            <DetailsTab form={form} />
          </TabsContent>
        </Tabs>
      </section>
    </>
  );
}
