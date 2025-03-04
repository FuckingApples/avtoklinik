"use client";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "~/components/ui/card";
import { Button } from "~/components/ui/button";
import { OrganizationCreationForm } from "~/components/forms/organization-creation";
import { useForm } from "react-hook-form";
import {
  organizationCreationSchema,
  type TOrganizationCreationSchema,
} from "~/utils/validation/organization-creation";
import { zodResolver } from "@hookform/resolvers/zod";
import { useRouter, useSearchParams } from "next/navigation";
import { useCreateOrganization } from "~/hooks/use-organization";

export default function NewOrganizationPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const createOrganization = useCreateOrganization();
  const form = useForm<TOrganizationCreationSchema>({
    resolver: zodResolver(organizationCreationSchema),
    defaultValues: {
      name: "",
    },
  });

  const handleSubmit = async (data: TOrganizationCreationSchema) => {
    await createOrganization.mutateAsync(data);
  };

  return (
    <div className="flex h-screen items-center justify-center">
      <Card className="w-[350px]">
        <CardHeader>
          <CardTitle>Создание организации</CardTitle>
          <CardDescription>Создайте новую команду в один клик</CardDescription>
        </CardHeader>
        <CardContent>
          <OrganizationCreationForm form={form} />
        </CardContent>
        <CardFooter className="flex justify-between">
          <Button
            onClick={() => router.back()}
            variant="outline"
            disabled={searchParams.has("first")}
          >
            Отмена
          </Button>
          <Button onClick={form.handleSubmit(handleSubmit)}>Создать</Button>
        </CardFooter>
      </Card>
    </div>
  );
}
