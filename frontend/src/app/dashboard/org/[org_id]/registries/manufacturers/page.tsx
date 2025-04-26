import { ManufacturersTable } from "~/components/tables/registries/manufacturers/table";

export default async function ManufacturersPage() {
  return (
    <div className="flex h-full flex-col w-full">
        <main className="flex flex-1 items-start gap-4 p-4 ">
            <section className="grid flex-1 items-center gap-2">
                <ManufacturersTable />
            </section>
        </main>
    </div>
  );
} 