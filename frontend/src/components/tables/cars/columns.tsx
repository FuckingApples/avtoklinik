"use client";

import type { DataTableRowAction } from "~/types/data-table";
import type { ColumnDef } from "@tanstack/react-table";
import {
  ArrowUpDown,
  CalendarIcon,
  CircleDashed,
  Clock,
  Ellipsis,
  Text,
} from "lucide-react";
import React from "react";
// import { DataTableColumnHeader } from "~/components/data-table-column-header";
import { Button } from "~/components/ui/button";
import { Checkbox } from "~/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import type { Car } from "~/types/car";
import { DataTableColumnHeader } from "~/components/ui/data-table/data-table-column-header";

interface GetCarsTableColumnsProps {
  setRowAction: React.Dispatch<
    React.SetStateAction<DataTableRowAction<Car> | null>
  >;
}

export function getCarsTableColumns({
  setRowAction,
}: GetCarsTableColumnsProps): ColumnDef<Car>[] {
  return [
    {
      id: "select",
      header: ({ table }) => (
        <Checkbox
          checked={
            table.getIsAllPageRowsSelected() ||
            (table.getIsSomePageRowsSelected() && "indeterminate")
          }
          onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
          aria-label="Select all"
          className="translate-y-0.5"
        />
      ),
      cell: ({ row }) => (
        <Checkbox
          checked={row.getIsSelected()}
          onCheckedChange={(value) => row.toggleSelected(!!value)}
          aria-label="Select row"
          className="translate-y-0.5"
        />
      ),
      enableSorting: false,
      enableHiding: false,
      size: 40,
    },
    {
      id: "car",
      accessorKey: "brand",
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Автомобиль" />
      ),
      cell: ({ row }) => {
        const originalRow = row.original;
        return (
          <>
            {originalRow.brand} {originalRow.model}
          </>
        );
      },
      enableSorting: false,
      enableHiding: false,
    },
    {
      id: "year",
      accessorKey: "year",
      meta: {
        label: "Год выпуска",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Год выпуска" />
      ),
    },
    {
      id: "license_plate",
      accessorKey: "license_plate",
      meta: {
        label: "Гос. номер",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Гос. номер" />
      ),
      enableSorting: false,
    },
    {
      id: "license_plate_region",
      accessorKey: "license_plate_region",
      meta: {
        label: "Страна регистрации",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Страна регистрации" />
      ),
      enableSorting: false,
    },
    {
      id: "client",
      accessorKey: "client",
      meta: {
        label: "Клиент",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Клиент" />
      ),
      cell: ({ row }) => {
        const client = row.original.client;

        if (!client) {
          return <>-</>;
        }
      },
      enableSorting: false,
    },
    {
      id: "vin",
      accessorKey: "vin",
      meta: {
        label: "VIN",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="VIN" />
      ),
    },
    {
      id: "frame",
      accessorKey: "frame",
      meta: {
        label: "Frame",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Frame" />
      ),
      cell: ({ row }) => {
        const frame = row.original.frame;

        if (!frame) {
          return <>-</>;
        }
      },
    },
    {
      id: "mileage",
      accessorKey: "mileage",
      meta: {
        label: "Пробег",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Пробег, км." />
      ),
      cell: ({ row }) => <>{row.getValue("mileage")}</>,
    },
    {
      id: "color",
      accessorKey: "color",
      meta: {
        label: "Цвет",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Цвет" />
      ),
      cell: ({ row }) => {
        const color = row.original.color;

        if (!color) {
          return <>-</>;
        }

        return (
          <div className="flex items-center gap-1.5">
            {color.hex && (
              <span
                style={{ backgroundColor: color.hex }}
                className="bg-muted border-border size-4 rounded-full border"
              />
            )}
            {color.name}
          </div>
        );
      },
      enableSorting: false,
    },
    {
      id: "actions",
      cell: function Cell({ row }) {
        return (
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button
                aria-label="Open menu"
                variant="ghost"
                className="data-[state=open]:bg-muted flex size-8 p-0"
              >
                <Ellipsis className="size-4" aria-hidden="true" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-40">
              <DropdownMenuItem
                onSelect={() => setRowAction({ row, variant: "view" })}
              >
                Просмотреть
              </DropdownMenuItem>
              <DropdownMenuItem
                onSelect={() => setRowAction({ row, variant: "update" })}
              >
                Редактировать
              </DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem
                onSelect={() => setRowAction({ row, variant: "delete" })}
              >
                Удалить
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        );
      },
      size: 40,
    },
  ];
}
