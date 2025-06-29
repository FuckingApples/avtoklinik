"use client";

import { ChevronRight, Folder, Plus, Grid, List, BookOpen } from "lucide-react";
import { Button } from "~/components/ui/button";
import { getRegistriesData } from "~/config/registries-content";
import Link from "next/link";
import React, { useState } from "react";
import { useParams } from "next/navigation";
import { useRegistriesCounts } from "~/hooks/use-registries";
import { HelpMenu } from "~/components/help-menu";

export default function RegistriesPage() {
  const params = useParams();
  const org_id = params.org_id as string;
  const [viewMode, setViewMode] = useState<string>("grid");

  const menuItems = getRegistriesData(org_id);
  const { data: counts, isLoading } = useRegistriesCounts();

  return (
    <div className="flex flex-1 items-center justify-center p-6">
      <div className="max-w-3xl">
        <div className="mb-10 text-center">
          <div className="mb-6 flex items-center justify-center">
            <div className="flex h-20 w-20 items-center justify-center rounded-full bg-white drop-shadow-[0_0_15px_rgba(0,0,0,0.15)]">
              <BookOpen size={32} />
            </div>
          </div>
          <h1 className="mb-4 text-3xl font-bold">Справочники</h1>
          <p className="text-muted-foreground mx-10 text-sm">
            Здесь вы можете управлять справочниками. Выберите категорию из
            списка ниже или воспользуйтесь боковым меню.
          </p>
        </div>

        <div className="mb-6 flex items-center justify-between">
          <Button variant="outline" className="w-32">
            <Plus className="h-4 w-4" />
            <span>Добавить</span>
          </Button>
          <div className="flex items-center rounded-md border p-1">
            <button
              className={`mr-1 flex h-8 w-8 items-center justify-center rounded-sm ${viewMode === "grid" ? "bg-accent text-accent-foreground" : "hover:bg-muted"}`}
              onClick={() => setViewMode("grid")}
            >
              <Grid className="h-4 w-4" />
            </button>
            <button
              className={`flex h-8 w-8 items-center justify-center rounded-sm ${viewMode === "list" ? "bg-accent text-accent-foreground" : "hover:bg-muted"}`}
              onClick={() => setViewMode("list")}
            >
              <List className="h-4 w-4" />
            </button>
          </div>
        </div>

        {viewMode === "grid" ? (
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2">
            {menuItems.map((section) => (
              <div
                key={section.title}
                className="rounded-lg border bg-white p-4 shadow-sm transition-colors hover:border-gray-300"
              >
                <div className="mb-3 flex items-center">
                  <div className="mr-3 flex h-10 w-10 items-center justify-center rounded-lg border border-blue-100 bg-gradient-to-br from-blue-50 to-blue-100 shadow-sm">
                    <Folder size={22} className="text-blue-500" />
                  </div>
                  <h3 className="text-lg font-semibold">{section.title}</h3>
                </div>
                <div>
                  {section.items.map((item) => {
                    const count = counts?.[item.path] ?? 0;

                    return (
                      <Link
                        key={item.title}
                        href={item.href}
                        className="flex items-center justify-between border-t py-2"
                      >
                        <span className="text-sm">{item.title}</span>
                        <div className="flex items-center">
                          <span className="mr-2 rounded-full bg-gray-100 px-2 py-0.5 text-xs text-gray-500">
                            {isLoading ? "..." : count}
                          </span>
                          <ChevronRight size={16} className="text-gray-400" />
                        </div>
                      </Link>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="rounded-lg border bg-white shadow-sm">
            <div className="border-b px-4 py-3">
              <h3 className="font-medium">Все справочники</h3>
            </div>
            <div className="divide-y">
              {menuItems.flatMap((section) =>
                section.items.map((item) => (
                  <Link
                    key={item.title}
                    href={item.href}
                    className="flex items-center justify-between px-4 py-3 hover:bg-gray-50"
                  >
                    <div className="flex items-center">
                      <div className="mr-3 flex h-9 w-9 items-center justify-center rounded-lg bg-gray-100 shadow-sm">
                        <Folder
                          size={16}
                          className="text-gray-500"
                          strokeWidth={2}
                        />
                      </div>
                      <div>
                        <div className="font-medium">{item.title}</div>
                        <div className="text-xs text-gray-500">
                          {section.title}
                        </div>
                      </div>
                    </div>
                    <ChevronRight size={16} className="text-gray-400" />
                  </Link>
                )),
              )}
            </div>
          </div>
        )}
      </div>
      <HelpMenu pageKey="registries" />
    </div>
  );
}
