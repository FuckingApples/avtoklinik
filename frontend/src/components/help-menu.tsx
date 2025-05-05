import { HelpCircle } from "lucide-react";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "~/components/ui/popover";
import { Button } from "~/components/ui/button";
import React from "react";
import { helpContent, getHelpContent } from "~/config/help-content";

export function HelpMenu({
  pageKey = "default",
}: {
  pageKey?: keyof typeof helpContent;
}) {
  const content = getHelpContent(pageKey);

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          size="icon"
          className="fixed right-5 bottom-5 rounded-full bg-blue-500 text-white hover:bg-blue-600 hover:text-white"
        >
          <HelpCircle />
        </Button>
      </PopoverTrigger>
      <PopoverContent
        className="w-100 bg-blue-50 p-0"
        align="end"
        sideOffset={10}
      >
        <div className="border-b border-blue-100 p-4">
          <h5 className="text-sm font-medium text-blue-800">{content.title}</h5>
        </div>
        <div className="divide-y divide-blue-100 px-4 py-2">
          {content.items.map((item, index) => (
            <div key={index} className="py-2">
              <h5 className="text-sm font-semibold text-blue-700">
                {item.title}
              </h5>
              <p className="mt-1 text-xs text-blue-600">{item.description}</p>
            </div>
          ))}
        </div>
      </PopoverContent>
    </Popover>
  );
}
