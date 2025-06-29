import { HelpCircle, ExternalLink } from "lucide-react";
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
        <div className="divide-y divide-blue-100">
          {content.items.map((item, index) => (
            <div
              key={index}
              className={`p-2 ${item.url ? "hover:bg-blue-100" : ""}`}
            >
              {item.url ? (
                <a href={item.url} target="_blank" rel="noopener noreferrer">
                  <div className="flex items-center justify-between px-2">
                    <h5 className="text-sm font-semibold text-blue-700">
                      {item.title}
                    </h5>
                    <ExternalLink size={14} className="text-blue-600" />
                  </div>
                  <p className="mt-1 px-2 text-xs text-blue-600">
                    {item.description}
                  </p>
                </a>
              ) : (
                <div className="px-2">
                  <h5 className="text-sm font-semibold text-blue-700">
                    {item.title}
                  </h5>
                  <p className="mt-1 text-xs text-blue-600">
                    {item.description}
                  </p>
                </div>
              )}
            </div>
          ))}
        </div>
      </PopoverContent>
    </Popover>
  );
}
