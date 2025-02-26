import React from "react";
import { cn } from "~/lib/utils";

export type InputProps = React.ComponentProps<"input"> & {
  startIcon?: React.JSX.Element;
  endIcon?: React.JSX.Element;
};

const Input = ({
  className,
  type,
  startIcon: StartIcon,
  endIcon: EndIcon,
  ...props
}: InputProps) => {
  return (
    <div data-slot="input" className="relative">
      {StartIcon && (
        <div className="pointer-events-none absolute inset-0 left-0 flex items-center pl-3">
          {StartIcon}
        </div>
      )}
      <input
        type={type}
        className={cn(
          "border-input bg-background ring-offset-background file:text-foreground placeholder:text-muted-foreground focus-visible:ring-ring flex h-10 w-full rounded-md border px-3 py-2 text-base file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-hidden disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          StartIcon && "pl-10",
          EndIcon && "pr-10",
          className,
        )}
        {...props}
      />
      {EndIcon && (
        <div className="pointer-events-none absolute top-1/2 right-0 flex -translate-y-1/2 items-center pr-3">
          {EndIcon}
        </div>
      )}
    </div>
  );
};

Input.displayName = "Input";
export { Input };
