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
      <UserInfoBanner
        className="mt-3"
        isDirty={form.formState.isDirty}
        onClear={() => {
          form.reset();
        }}
      />
      <section className="mx-auto flex flex-col lg:max-w-5xl">
        <Tabs
          defaultValue={page}
          onValueChange={setPage}
          className="overflow-visible"
        >
          <div className="flex flex-col justify-between md:flex-row md:items-center">
            <div className="mx-3">
              <h3 className="text-foreground text-2xl leading-none font-bold">
                Настройки
              </h3>
              <span className="text-muted-foreground text-sm">
                Настройте свой профиль
              </span>
            </div>
            <ScrollArea>
              <TabsList className="m-3">
                <TabsTrigger value="details">Мои данные</TabsTrigger>
                <TabsTrigger value="security">Безопасность</TabsTrigger>
                <TabsTrigger value="apperance">Внешний вид</TabsTrigger>
                <TabsTrigger value="notifications">Уведомления</TabsTrigger>
              </TabsList>
              <ScrollBar orientation="horizontal" className="hidden" />
            </ScrollArea>
          </div>
          <TabsContent value="details" className="mx-3">
            <DetailsTab form={form} />
          </TabsContent>
        </Tabs>
      </section>
    </>
  );
}
