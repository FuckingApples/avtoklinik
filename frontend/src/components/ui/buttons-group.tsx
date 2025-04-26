import React from "react";
import { cn } from "~/lib/utils";
import type { Button, buttonVariants } from "~/components/ui/button";
import type { VariantProps } from "class-variance-authority";

interface ButtonGroupProps
  extends React.ComponentProps<"div">,
    VariantProps<typeof buttonVariants> {
  orientation?: "horizontal" | "vertical";
  children?: React.ReactElement<React.ComponentProps<typeof Button>>[];
}

function ButtonsGroup({
  children,
  className,
  orientation = "horizontal",
  variant,
  size,
  ...props
}: ButtonGroupProps) {
  const buttonsCount = React.Children.count(children);
  const isHorizontal = orientation === "horizontal";
  const isVertical = orientation === "vertical";

  return (
    <div
      className={cn(
        "flex",
        {
          "w-fit flex-col": isVertical,
          "divide-muted divide-x": isHorizontal,
        },
        className,
      )}
      {...props}
    >
      {React.Children.map(children, (child, index) => {
        if (!React.isValidElement(child)) return null;

        const isFirst = index === 0;
        const isLast = index === buttonsCount - 1;
        return React.cloneElement(child, {
          className: cn(
            {
              "rounded-s-none": isHorizontal && !isFirst,
              "rounded-e-none": isHorizontal && !isLast,
              "border-s-0": isHorizontal && !isFirst,

              "rounded-t-none": isVertical && !isFirst,
              "rounded-b-none": isVertical && !isLast,
              "border-t-0": isVertical && !isFirst,
            },
            child.props.className,
          ),
          variant: child.props.variant ?? variant,
          size: child.props.size ?? size,
        });
      })}
    </div>
  );
}

export { ButtonsGroup };
