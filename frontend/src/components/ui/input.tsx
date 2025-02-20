import React from "react";
import { cn } from "~/lib/utils";

export type InputProps = React.ComponentProps<"input"> & {
  startIcon?: React.JSX.Element;
  endIcon?: React.JSX.Element;
};

const Input = React.forwardRef<HTMLInputElement, InputProps>(
  (
    { className, type, startIcon: StartIcon, endIcon: EndIcon, ...props },
    ref,
  ) => {
    return (
      <div className="relative">
        {StartIcon && (
          <div className="pointer-events-none absolute inset-0 left-0 flex items-center pl-3">
            {StartIcon}
          </div>
        )}
        <input
          type={type}
          className={cn(
            "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-base ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
            StartIcon && "pl-10",
            EndIcon && "pr-10",
            className,
          )}
          ref={ref}
          {...props}
        />
        {EndIcon && (
          <div className="pointer-events-none absolute right-0 top-1/2 flex -translate-y-1/2 items-center pr-3">
            {EndIcon}
          </div>
        )}
      </div>
    );
  },
);

Input.displayName = "Input";
export { Input };
