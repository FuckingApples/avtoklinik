import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
} from "~/components/ui/form";
import type { UseFormReturn } from "react-hook-form";
import type { TUserSettingsSchema } from "~/utils/validation/user-settings";
import { RadioGroup, RadioGroupItem } from "~/components/ui/radio-group";
import { useTheme } from "next-themes";
import { Label } from "~/components/ui/label";
import { Card } from "~/components/ui/card";
import { cn } from "~/lib/utils";
import { useEffect, useState } from "react";

export default function AppearanceTab({
  form,
}: {
  form: UseFormReturn<TUserSettingsSchema>;
}) {
  const { theme, systemTheme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return null;
  }

  return (
    <Form {...form}>
      <form id="user-settings">
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem className="md:flex">
              <div className="flex-1">
                <FormLabel>Тема</FormLabel>
                <FormDescription>
                  Выберите предпочтительные цвета интерфейса
                </FormDescription>
              </div>
              <FormControl className="grid grid-cols-2 md:flex-2">
                <RadioGroup onValueChange={setTheme} value={theme}>
                  {["light", "dark", "black", "system"].map((themeOption) => (
                    <Label
                      className="[&:has(:checked)]:ring-primary w-full rounded-xl [&:has(:checked)]:ring-2"
                      htmlFor={themeOption}
                      key={themeOption}
                    >
                      <RadioGroupItem
                        value={themeOption}
                        id={themeOption}
                        className="hidden"
                      />
                      <Card className="flex cursor-pointer flex-col items-center justify-between gap-2 p-2">
                        <div
                          className={cn(
                            themeOption !== "system"
                              ? themeOption
                              : systemTheme,
                            "bg-primary-foreground border-border text-foreground flex aspect-video w-full grow rounded-md border",
                          )}
                        >
                          <div className="bg-sidebar flex h-full w-1/4 flex-col gap-0.5 rounded-l-md p-1">
                            <div className="mb-1 flex items-center gap-1">
                              <span className="bg-sidebar-primary flex h-2 w-2 rounded-full" />
                              <div className="flex grow flex-col gap-0.5">
                                <span className="bg-sidebar-foreground flex h-0.5 w-full rounded-full" />
                                <span className="bg-sidebar-foreground flex h-0.5 w-1/2 rounded-full" />
                              </div>
                            </div>
                            <span className="bg-sidebar-accent flex h-1.5 w-full rounded-full" />
                            <span className="bg-sidebar-accent flex h-1.5 w-full rounded-full" />
                            <span className="bg-sidebar-accent flex h-1.5 w-full rounded-full" />
                            <span className="bg-sidebar-accent flex h-1.5 w-full rounded-full" />
                            <span className="bg-sidebar-accent flex h-1.5 w-full rounded-full" />
                            <span className="bg-sidebar-accent flex h-1.5 w-full rounded-full" />
                            <span className="grow" />
                            <span className="bg-sidebar-accent flex h-1 w-1/2 rounded-full" />
                            <span className="bg-sidebar-accent flex h-1 w-1/2 rounded-full" />
                            <div className="mt-1 flex items-center gap-1">
                              <span className="bg-sidebar-primary flex h-2 w-2 rounded-full" />
                              <div className="flex grow flex-col gap-0.5">
                                <span className="bg-sidebar-foreground flex h-0.5 w-full rounded-full" />
                                <span className="bg-sidebar-foreground flex h-0.5 w-1/2 rounded-full" />
                              </div>
                            </div>
                          </div>
                          <div className="bg-background my-0.5 mr-0.5 w-full rounded" />
                        </div>
                        <span className="text-sm capitalize">
                          {themeOption}
                        </span>
                      </Card>
                    </Label>
                  ))}
                </RadioGroup>
              </FormControl>
            </FormItem>
          )}
        />
      </form>
    </Form>
  );
}
