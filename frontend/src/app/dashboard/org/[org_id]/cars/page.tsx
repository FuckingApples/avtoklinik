import { CarsTable } from "~/components/tables/cars/table";
import DashboardHeader from "~/components/ui/dashboard-header";
import { ChevronDownIcon, PlusIcon } from "lucide-react";
import { Button } from "~/components/ui/button";
import { ButtonsGroup } from "~/components/ui/buttons-group";
import {
  DropdownMenu,
  DropdownMenuContent,
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
              <DropdownMenuContent align="end"></DropdownMenuContent>
            </DropdownMenu>
          </ButtonsGroup>
        </DashboardHeader.ActionButton>
        {/*<div className="flex items-center gap-3">*/}
        {/*  <Input*/}
        {/*    className="h-9 w-[400px]"*/}
        {/*    placeholder="Поиск по VIN, номеру, марке..."*/}
        {/*    value={search || ""}*/}
        {/*    onChange={(e) => setSearch(e.target.value)}*/}
        {/*    startIcon={<Search className="size-4" />}*/}
        {/*  />*/}

        {/*  /!*<Button*!/*/}
        {/*  /!*  variant="outline"*!/*/}
        {/*  /!*  size="sm"*!/*/}
        {/*  /!*  onClick={() => setIsFiltersOpen(true)}*!/*/}
        {/*  /!*  className="inline-flex h-9 items-center"*!/*/}
        {/*  /!*>*!/*/}
        {/*  /!*  <span className="flex items-center pr-2">*!/*/}
        {/*  /!*    <Filter*!/*/}
        {/*  /!*      className={*!/*/}
        {/*  /!*        Object.keys(filters).length > 0*!/*/}
        {/*  /!*          ? "text-primary mr-1.5 size-4"*!/*/}
        {/*  /!*          : "mr-1.5 size-4"*!/*/}
        {/*  /!*      }*!/*/}
        {/*  /!*    />*!/*/}
        {/*  /!*    Фильтры*!/*/}
        {/*  /!*    {Object.keys(filters).length > 0 && (*!/*/}
        {/*  /!*      <Badge*!/*/}
        {/*  /!*        variant="secondary"*!/*/}
        {/*  /!*        className="ml-1.5 h-5 px-1.5 py-0 text-xs"*!/*/}
        {/*  /!*      >*!/*/}
        {/*  /!*        {Object.keys(filters).length}*!/*/}
        {/*  /!*      </Badge>*!/*/}
        {/*  /!*    )}*!/*/}
        {/*  /!*  </span>*!/*/}
        {/*  /!*</Button>*!/*/}
        {/*  <Button*/}
        {/*    variant="outline"*/}
        {/*    size="sm"*/}
        {/*    onClick={() => setIsTableSettingsOpen(true)}*/}
        {/*    className="inline-flex h-9 items-center"*/}
        {/*  >*/}
        {/*    <span className="flex items-center pr-2">*/}
        {/*      <Settings className="mr-1.5 size-4" />*/}
        {/*      Настройки таблицы*/}
        {/*    </span>*/}
        {/*  </Button>*/}
        {/*  <Button*/}
        {/*    size="sm"*/}
        {/*    onClick={handleAddCar}*/}
        {/*    className="inline-flex h-9 items-center"*/}
        {/*  >*/}
        {/*    <span className="flex items-center pr-2">*/}
        {/*      <Plus className="mr-1.5 size-4" />*/}
        {/*      Добавить автомобиль*/}
        {/*    </span>*/}
        {/*  </Button>*/}
        {/*</div>*/}
      </DashboardHeader>

      <main className="flex flex-1 items-start gap-4 p-6 md:py-8">
        <section className="grid flex-1 items-center gap-2">
          <CarsTable />
        </section>
        {/*<span className="bg-muted h-[500px] w-[600px]" />*/}
      </main>

      {/*<CarTableSettingsDialog*/}
      {/*  open={isTableSettingsOpen}*/}
      {/*  onClose={() => setIsTableSettingsOpen(false)}*/}
      {/*  settings={settings}*/}
      {/*  onSave={saveSettings}*/}
      {/*/>*/}

      {/*<CarFiltersDialog*/}
      {/*  open={isFiltersOpen}*/}
      {/*  onClose={() => setIsFiltersOpen(false)}*/}
      {/*  filterOptions={filterOptions}*/}
      {/*  initialFilters={filters}*/}
      {/*  onApplyFilters={applyFilters}*/}
      {/*/>*/}

      {/*<CarForm*/}
      {/*  open={isCarFormOpen}*/}
      {/*  onClose={() => setIsCarFormOpen(false)}*/}
      {/*  onSubmit={async (carData) => {*/}
      {/*    if (editingCar && selectedCar && editingCar.id === selectedCar.id) {*/}
      {/*      const updatedCar = await getCar(org_id as string, editingCar.id);*/}
      {/*      setSelectedCar(updatedCar);*/}
      {/*    }*/}
      {/*  }}*/}
      {/*  car={editingCar}*/}
      {/*  orgId={org_id as string}*/}
      {/*/>*/}

      {/*<DeleteCar*/}
      {/*  open={deleteDialogOpen}*/}
      {/*  onOpenChange={setDeleteDialogOpen}*/}
      {/*  onConfirm={() => {}}*/}
      {/*  car={carInfo}*/}
      {/*/>*/}
    </div>
  );
}
