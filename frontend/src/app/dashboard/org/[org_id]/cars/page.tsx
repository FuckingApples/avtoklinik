import { CarsTable } from "~/components/tables/cars/table";
import DashboardHeader from "~/components/ui/dashboard-header";
import { ChevronDownIcon, FileUpIcon, PlusIcon } from "lucide-react";
import { Button } from "~/components/ui/button";
import { ButtonsGroup } from "~/components/ui/buttons-group";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";

export default async function CarsPage() {
  return (
    <div className="flex h-full flex-col">
      <DashboardHeader>
        <DashboardHeader.Title>Автомобили</DashboardHeader.Title>
        <DashboardHeader.ActionButton asChild>
          <ButtonsGroup>
            <Button>
              <PlusIcon />
              <span className="hidden sm:block">Добавить автомобиль</span>
            </Button>
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button size="sm" className="rounded-l-none">
                  <ChevronDownIcon />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" sideOffset={4}>
                <DropdownMenuItem>
                  <FileUpIcon />
                  Экспортировать из файла
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </ButtonsGroup>
        </DashboardHeader.ActionButton>
      </DashboardHeader>

      <main className="flex flex-1 items-start gap-4 p-4 md:py-8">
        <section className="grid flex-1 items-center gap-2">
          <CarsTable />
        </section>
        {/*<span className="bg-muted h-[500px] w-[600px]" />*/}
      </main>
    </div>
  );
}
