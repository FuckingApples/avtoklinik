import { SidebarTrigger } from "~/components/ui/sidebar";
import { Separator } from "~/components/ui/separator";
import React from "react";
import { Button } from "~/components/ui/button";
import { Slot } from "radix-ui";

const Title = ({ children }: React.PropsWithChildren) => (
  <h2 className="text-lg font-semibold">{children}</h2>
);

interface ActionButtonProps extends React.ComponentProps<typeof Button> {
  asChild?: boolean;
}

const ActionButton = ({
  asChild = false,
  ...props
}: React.PropsWithChildren<ActionButtonProps>) => {
  const Comp = asChild ? Slot.Root : Button;
  return <Comp {...props} size="sm" />;
};

function DashboardHeader({ children }: React.PropsWithChildren) {
  const childrenArray = React.Children.toArray(children);

  const title = React.useMemo(
    () =>
      childrenArray.find(
        (child) => React.isValidElement(child) && child.type === Title,
      ),
    [childrenArray],
  );

  const actionButton = React.useMemo(
    () =>
      childrenArray.find(
        (child) => React.isValidElement(child) && child.type === ActionButton,
      ),
    [childrenArray],
  );

  return (
    <header className="border-border flex h-16 shrink-0 items-center justify-between gap-2 border-b px-4 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
      <div className="flex items-center justify-center gap-2">
        <SidebarTrigger className="-ml-1" />
        <Separator orientation="vertical" className="mr-2 h-4!" />
        {title}
      </div>
      {actionButton}
    </header>
  );
}

DashboardHeader.Title = Title;
DashboardHeader.ActionButton = ActionButton;

export default DashboardHeader;
