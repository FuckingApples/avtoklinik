import { Form } from "~/components/ui/form";
import type { UseFormReturn } from "react-hook-form";
import { type TOrganizationCreationSchema } from "~/utils/validation/organization-creation";
import React from "react";
import {
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "~/components/ui/form";
import { Input } from "~/components/ui/input";

export const OrganizationCreationForm = ({
  form,
}: React.PropsWithoutRef<{
  form: UseFormReturn<TOrganizationCreationSchema>;
}>) => {
  return (
    <Form {...form}>
      <form>
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Название</FormLabel>
              <FormControl>
                <Input
                  placeholder="ООО «Рога и Копыта»"
                  autoComplete="organization"
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
      </form>
    </Form>
  );
};
