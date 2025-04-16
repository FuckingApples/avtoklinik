"use client";

import React from "react";
import type { DataTableRowAction } from "~/types/data-table";
import type { Car } from "~/types/car";
import { getCarsTableColumns } from "./columns";
import { useDataTable } from "~/hooks/use-data-table";
import { useCars } from "~/hooks/use-cars";
import { DataTable } from "~/components/ui/data-table";
import { CarDetails } from "~/components/sidebars/car-details";
import { useCarsStore } from "~/store/cars";
import { parseAsInteger, useQueryStates } from "nuqs";
import { getFiltersStateParser, getSortingStateParser } from "~/lib/parsers";
import { DataTableToolbar } from "~/components/ui/data-table/data-table-toolbar";
import { DataTableSortList } from "~/components/ui/data-table/data-table-sort-list";

export function CarsTable() {
  const { setFilters } = useCarsStore();
  const [search] = useQueryStates({
    page: parseAsInteger.withDefault(1),
    perPage: parseAsInteger.withDefault(10),
    sort: getSortingStateParser<Car>().withDefault([]),
    filters: getFiltersStateParser().withDefault([]),
  });

  const { data, isLoading } = useCars();
  const cars = data?.results ?? [];
  const rowCount = data?.count ?? 0;

  const [rowAction, setRowAction] =
    React.useState<DataTableRowAction<Car> | null>(null);

  const columns = React.useMemo(
    () => getCarsTableColumns({ setRowAction }),
    [],
  );

  const { table, shallow, debounceMs } = useDataTable({
    data: cars,
    columns,
    getRowId: (originalRow) => originalRow.id,
    rowCount,
    initialState: {
      columnPinning: { right: ["actions"] },
    },
    shallow: false,
    clearOnDefault: true,
  });

  React.useEffect(() => {
    setFilters({
      page: search.page,
      page_size: search.perPage,
      ordering: search.sort.map((s) => `${s.desc ? "-" : ""}${s.id}`).join(","),
    });
  }, [search.page, search.perPage, search.sort, setFilters]);

  return (
    <>
      <DataTable table={table}>
        <DataTableToolbar table={table}>
          <DataTableSortList table={table} align="end" />
        </DataTableToolbar>
      </DataTable>
      <CarDetails
        car={rowAction?.row.original ?? null}
        open={rowAction?.variant === "view"}
        onClose={() => {}}
        onEdit={() => {}}
        onDelete={() => {}}
      />
    </>
  );
}
