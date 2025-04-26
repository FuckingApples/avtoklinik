"use client";

import {
  ChevronRight,
  ChevronDown,
  Search
} from "lucide-react";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "~/components/ui/collapsible";
import { getRegistriesData } from "~/config/registries";
import Link from "next/link";
import React, { useState } from "react";
import { useParams, usePathname } from "next/navigation";

export function RegistriesNavigation() {
  const pathname = usePathname();
  const params = useParams();
  const org_id = params.org_id as string;

  const [openSections, setOpenSections] = useState<Record<string, boolean>>({});
  const [searchTerm, setSearchTerm] = useState<string>("");
  
  const menuItems = getRegistriesData(org_id);

  const isActive = (href: string) => {
    if (pathname === href) return true;
    return pathname.startsWith(href);
  };

  const toggleSection = (sectionTitle: string) => {
    setOpenSections(prev => ({
      ...prev,
      [sectionTitle]: !prev[sectionTitle]
    }));
  };

  const filteredRegistriesLinks = searchTerm.trim() === "" 
    ? menuItems
    : menuItems.map(section => ({
        ...section,
        items: section.items.filter(item => 
          item.title.toLowerCase().includes(searchTerm.toLowerCase())
        )
      })).filter(section => section.items.length > 0);

  return (
    <div className="border-r">
      <div className="p-3">
        <div className="relative">
          <div className="absolute left-2.5 top-1/2 -translate-y-1/2 text-gray-400">
            <Search className="w-4 h-4" />
          </div>
          <input
            placeholder="Поиск..."
            className="h-9 pl-8 rounded-md border"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      <nav>
        {filteredRegistriesLinks.map((section) => (
          <Collapsible
            key={section.title}
            open={openSections[section.title]}
            onOpenChange={() => toggleSection(section.title)}
          >
            <CollapsibleTrigger className="flex w-full items-center px-4 py-2 text-sm font-medium hover:bg-gray-50">
              {openSections[section.title] ? (
                <ChevronDown className="h-4 w-4 mr-2" />
              ) : (
                <ChevronRight className="h-4 w-4 mr-2" />
              )}
              <span>{section.title}</span>
            </CollapsibleTrigger>
            <CollapsibleContent>
              <div className="pl-10">
                {section.items.map((item) => (
                  <Link
                    key={item.title}
                    href={item.href}
                    className={`flex items-center justify-between px-4 py-2 my-1 text-sm mr-2 rounded-md ${
                      isActive(item.href)
                        ? "bg-gray-50 text-black font-medium"
                        : "text-gray-600 hover:bg-gray-50"
                    }`}
                  >
                    <span>{item.title}</span>
                    <span className="text-xs bg-gray-100 rounded-full px-2 py-0.5 text-gray-500">
                      {item.count}
                    </span>
                  </Link>
                ))}
              </div>
            </CollapsibleContent>
          </Collapsible>
        ))}
      </nav>
    </div>
  );
} 