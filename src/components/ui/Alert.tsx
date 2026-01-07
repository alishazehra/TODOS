"use client";

import * as React from "react";
import { cn } from "@/lib/utils";

interface AlertProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "default" | "destructive";
}

export const Alert = React.forwardRef<HTMLDivElement, AlertProps>(
  ({ className, variant = "default", children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        role="alert"
        className={cn(
          "relative w-full rounded-lg border p-4",
          variant === "destructive" &&
            "border-red-500/50 text-red-600 dark:border-red-500",
          className
        )}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Alert.displayName = "Alert";
