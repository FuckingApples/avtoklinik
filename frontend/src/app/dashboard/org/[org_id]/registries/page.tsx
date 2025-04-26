"use client";

import {
  ChevronRight,
  Folder,
  Plus,
  Grid,
  List,
  BookOpen,
} from "lucide-react";
import { Button } from "~/components/ui/button";
import { getRegistriesData } from "~/config/registries";
import Link from "next/link";
import React, { useState } from "react";
import { useParams } from "next/navigation";

export default function RegistriesPage() {
  const params = useParams();
  const org_id = params.org_id as string;
  const [viewMode, setViewMode] = useState<string>("grid");

  const menuItems = getRegistriesData(org_id);

  return (
    <div className="flex-1 flex items-center justify-center p-6">
      <div className="max-w-3xl">
        <div className="mb-10 text-center">
          <div className="mb-6 flex items-center justify-center">
            <div className="flex h-20 w-20 items-center justify-center rounded-full bg-white drop-shadow-[0_0_15px_rgba(0,0,0,0.15)]">
              <BookOpen size={32} />
            </div>
          </div>
          <h1 className="text-3xl font-bold mb-4">Справочники</h1>
          <p className="text-muted-foreground text-sm mx-10">
            Здесь вы можете управлять справочниками. Выберите
            категорию из списка ниже или воспользуйтесь боковым меню.
          </p>
        </div>

        <div className="flex items-center justify-between mb-6">
          <Button variant="outline" className="w-32">
            <Plus className="h-4 w-4" />
            <span>Добавить</span>
          </Button>
          <div className="flex items-center rounded-md border p-1">
            <button
              className={`flex h-8 w-8 mr-1 items-center justify-center rounded-sm ${viewMode === 'grid' ? 'bg-accent text-accent-foreground' : 'hover:bg-muted'}`}
              onClick={() => setViewMode('grid')}
            >
              <Grid className="h-4 w-4" />
            </button>
            <button
              className={`flex h-8 w-8 items-center justify-center rounded-sm ${viewMode === 'list' ? 'bg-accent text-accent-foreground' : 'hover:bg-muted'}`}
              onClick={() => setViewMode('list')}
            >
              <List className="h-4 w-4" />
            </button>
          </div>
        </div>

        {viewMode === "grid" ? (
          <div className="grid gap-6 grid-cols-1 md:grid-cols-2">
            {menuItems.map(section => (
              <div key={section.title} className="bg-white rounded-lg border shadow-sm p-4 hover:border-gray-300 transition-colors">
                <div className="flex items-center mb-3">
                  <div className="mr-3 flex h-10 w-10 items-center justify-center rounded-lg bg-gradient-to-br from-blue-50 to-blue-100 shadow-sm border border-blue-100">
                    <Folder size={22} className="text-blue-500" />
                  </div>
                  <h3 className="text-lg font-semibold">{section.title}</h3>
                </div>
                <div>
                  {section.items.map(item => (
                    <Link
                      key={item.title}
                      href={item.href}
                      className="flex items-center justify-between py-2 border-t"
                    >
                      <span className="text-sm">{item.title}</span>
                      <div className="flex items-center">
                        <span className="text-xs bg-gray-100 rounded-full px-2 py-0.5 mr-2 text-gray-500">{item.count}</span>
                        <ChevronRight size={16} className="text-gray-400" />
                      </div>
                    </Link>
                  ))}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="bg-white rounded-lg border shadow-sm">
            <div className="px-4 py-3 border-b">
              <h3 className="font-medium">Все справочники</h3>
            </div>
            <div className="divide-y">
              {menuItems.flatMap(section =>
                section.items.map(item => (
                  <Link
                    key={item.title}
                    href={item.href}
                    className="flex items-center justify-between px-4 py-3 hover:bg-gray-50"
                  >
                    <div className="flex items-center">
                      <div className="mr-3 flex h-9 w-9 items-center justify-center rounded-lg bg-gray-100 shadow-sm">
                        <Folder size={16} className="text-gray-500" strokeWidth={2} />
                      </div>
                      <div>
                        <div className="font-medium">{item.title}</div>
                        <div className="text-xs text-gray-500">{section.title}</div>
                      </div>
                    </div>
                    <ChevronRight size={16} className="text-gray-400" />
                  </Link>
                ))
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
