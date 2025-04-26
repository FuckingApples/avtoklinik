"use client";

import React from "react";
import type { DataTableRowAction } from "~/types/data-table";
import { MeasurementUnit } from "~/types/registries";
import { getMeasurementUnitsTableColumns } from "./columns";
import { useDataTable } from "~/hooks/use-data-table";
import { useMeasurementUnits } from "~/hooks/use-registries";
import { DataTable } from "~/components/ui/data-table";
import { useMeasurementUnitsStore } from "~/store/registries";
import { parseAsInteger, useQueryStates } from "nuqs";
import { getFiltersStateParser, getSortingStateParser } from "~/lib/parsers";
import { DataTableToolbar } from "~/components/ui/data-table/data-table-toolbar";
import { DataTableSortList } from "~/components/ui/data-table/data-table-sort-list";

export function MeasurementUnitsTable() {
  const { setFilters } = useMeasurementUnitsStore();
  const [search] = useQueryStates({
    page: parseAsInteger.withDefault(1),
    perPage: parseAsInteger.withDefault(10),
    sort: getSortingStateParser<MeasurementUnit>().withDefault([]),
    filters: getFiltersStateParser().withDefault([]),
  });

  const { data, isLoading } = useMeasurementUnits();
  const measurementUnits = data?.results ?? [];
  const rowCount = data?.count ?? 0;

  const [rowAction, setRowAction] =
    React.useState<DataTableRowAction<MeasurementUnit> | null>(null);

  const columns = React.useMemo(
    () => getMeasurementUnitsTableColumns({ setRowAction }),
    [],
  );

  const { table, shallow, debounceMs } = useDataTable({
    data: measurementUnits,
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
    </>
  );
}
