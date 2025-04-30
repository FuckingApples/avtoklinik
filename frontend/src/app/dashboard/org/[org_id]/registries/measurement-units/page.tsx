import { MeasurementUnitsTable } from "~/components/tables/registries/measurement-units/table";

export default async function MeasurementUnitsPage() {
  return (
    <div className="flex h-full w-full flex-col">
      <main className="flex flex-1 items-start gap-4 p-4">
        <section className="grid flex-1 items-center gap-2">
          <MeasurementUnitsTable />
        </section>
      </main>
    </div>
  );
}
