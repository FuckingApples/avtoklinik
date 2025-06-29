import { ManufacturersTable } from "~/components/tables/registries/manufacturers/table";
import { HelpMenu } from "~/components/help-menu";

export default async function ManufacturersPage() {
  return (
    <div className="flex h-full w-full flex-col">
      <main className="flex flex-1 items-start gap-4 p-4">
        <section className="grid flex-1 items-center gap-2">
          <ManufacturersTable />
        </section>
      </main>
      <HelpMenu pageKey="manufacturers" />
    </div>
  );
}
