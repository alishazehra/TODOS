"use client";

import * as React from "react";
import { cn } from "@/lib/utils";

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ className, type, label, error, id, ...props }, ref) => {
    const id = React.useId(); // always at top
const isConditionMet = someCondition;

return (
  <input id={isConditionMet ? id : undefined} ... />
);

    return (
      <div className="w-full">
        {label && (
          <label htmlFor={inputId} className="form-label mb-2 block">
            {label}
          </label>
        )}
        <input
          type={type}
          id={inputId}
          className={cn(
            "form-input",
            error && "border-red-500 focus:ring-red-500",
            className
          )}
          ref={ref}
          {...props}
        />
        {error && <p className="form-error">{error}</p>}
      </div>
    );
  }
);

Input.displayName = "Input";
