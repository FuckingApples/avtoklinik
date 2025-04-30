"use client";

import type { DataTableRowAction } from "~/types/data-table";
import type { ColumnDef } from "@tanstack/react-table";
import { Ellipsis } from "lucide-react";
import React from "react";
import { Button } from "~/components/ui/button";
import { Checkbox } from "~/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "~/components/ui/dropdown-menu";
import type { Equipment } from "~/types/registries";
import { DataTableColumnHeader } from "~/components/ui/data-table/data-table-column-header";

interface GetEquipmentsTableColumnsProps {
  setRowAction: React.Dispatch<
    React.SetStateAction<DataTableRowAction<Equipment> | null>
  >;
}

export function getEquipmentsTableColumns({
  setRowAction,
}: GetEquipmentsTableColumnsProps): ColumnDef<Equipment>[] {
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
        label: "Комплектность",
      },
      header: ({ column }) => (
        <DataTableColumnHeader column={column} title="Комплектность" />
      ),
      enableSorting: true,
      enableHiding: false,
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
