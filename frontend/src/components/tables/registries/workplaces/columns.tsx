"use client";

import type { DataTableRowAction } from "~/types/data-table";
import type { ColumnDef } from "@tanstack/react-table";
import { Ellipsis } from "lucide-react";
import React from "react";
import Image from "next/image";
import { Button } from "~/components/ui/button";
import { Checkbox } from "~/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import type { Workplace } from "~/types/registries";
import { DataTableColumnHeader } from "~/components/ui/data-table/data-table-column-header";

interface GetMeasurementUnitsTableColumnsProps {
  setRowAction: React.Dispatch<
    React.SetStateAction<DataTableRowAction<Workplace> | null>
  >;
}

export function getWorkplacesTableColumns({
  setRowAction,
}: GetMeasurementUnitsTableColumnsProps): ColumnDef<Workplace>[] {
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
      id: "name",
      accessorKey: "name",
      meta: {
        label: "Рабочее место",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Рабочее место" />
      ),
      enableSorting: true,
      enableHiding: false,
    },
    {
      id: "style",
      accessorKey: "style",
      meta: {
        label: "Оформление",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Оформление" />
      ),
      cell: ({ row }) => {
        const color = row.original.color;
        const icon = row.original.icon;
        return (
          <div
            className="h-7 w-14 rounded-full"
            style={{ backgroundColor: color }}
          >
            {icon ? (
              <div className="h-7 w-7 overflow-hidden rounded-full">
                <Image
                  src={icon}
                  alt="Изображение"
                  className="h-full w-full object-cover"
                />
              </div>
            ) : (
              <div className="flex h-7 w-7 items-center justify-center rounded-full bg-white/30">
                <span className="text-xs text-white">?</span>
              </div>
            )}
          </div>
        );
      },
      enableSorting: false,
    },
    {
      id: "description",
      accessorKey: "description",
      meta: {
        label: "Описание",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Описание" />
      ),
      enableSorting: true,
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
