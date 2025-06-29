import { EquipmentsTable } from "~/components/tables/registries/equipments/table";
import { HelpMenu } from "~/components/help-menu";

export default async function EquipmentsPage() {
  return (
    <div className="flex h-full w-full flex-col">
      <main className="flex flex-1 items-start gap-4 p-4">
        <section className="grid flex-1 items-center gap-2">
          <EquipmentsTable />
        </section>
      </main>
      <HelpMenu pageKey="equipments" />
    </div>
  );
}
