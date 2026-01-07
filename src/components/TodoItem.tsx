"use client";

import { useState } from "react";
import { Todo } from "@/types";
import { formatDate, cn } from "@/lib/utils";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";

interface TodoItemProps {
  todo: Todo;
  onToggle: (todo: Todo) => void;
  onDelete: (todo: Todo) => void;
  onUpdate: (todo: Todo, description: string) => void;
}

export function TodoItem({ todo, onToggle, onDelete, onUpdate }: TodoItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editDescription, setEditDescription] = useState(todo.description);
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

  const handleEditSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (editDescription.trim() && editDescription !== todo.description) {
      onUpdate(todo, editDescription.trim());
    }
    setIsEditing(false);
  };

  return (
    <div
      className={cn(
        "flex items-center gap-3 p-4 bg-white rounded-lg border shadow-sm transition-all",
        todo.completed && "bg-muted/50"
      )}
    >
      {/* Checkbox for toggle */}
      <button
        type="button"
        onClick={() => onToggle(todo)}
        className={cn(
          "h-5 w-5 rounded border-2 flex items-center justify-center transition-colors",
          todo.completed
            ? "bg-primary border-primary text-white"
            : "border-input hover:border-primary"
        )}
      >
        {todo.completed && (
          <svg
            className="h-3 w-3"
            fill="none"
            stroke="currentColor"
            strokeWidth={3}
            viewBox="0 0 24 24"
          >
            <path d="M5 13l4 4L19 7" />
          </svg>
        )}
      </button>

      {/* Description */}
      <div className="flex-1 min-w-0">
        {isEditing ? (
          <form onSubmit={handleEditSubmit}>
            <Input
              value={editDescription}
              onChange={(e) => setEditDescription(e.target.value)}
              onBlur={handleEditSubmit}
              autoFocus
              className="h-8"
            />
          </form>
        ) : (
          <p
            className={cn(
              "text-sm font-medium truncate cursor-pointer hover:text-primary",
              todo.completed && "line-through text-muted-foreground"
            )}
            onClick={() => setIsEditing(true)}
          >
            {todo.description}
          </p>
        )}
        <p className="text-xs text-muted-foreground mt-1">
          {formatDate(todo.createdAt)}
        </p>
      </div>

      {/* Actions */}
      <div className="flex items-center gap-1">
        <Button
          type="button"
          variant="ghost"
          size="sm"
          onClick={() => setIsEditing(!isEditing)}
          className="h-8 px-3 text-sm font-medium text-blue-600 hover:text-blue-700"
        >
          Edit
        </Button>

        {showDeleteConfirm ? (
          <div className="flex items-center gap-1">
            <Button
              type="button"
              variant="ghost"
              size="sm"
              onClick={() => onDelete(todo)}
              className="h-8 text-red-500 hover:text-red-600 "
            >
              Yes
            </Button>
            <Button
              type="button"
              variant="ghost"
              size="sm"
              onClick={() => setShowDeleteConfirm(false)}
              className="h-8"
            >
              No
            </Button>
          </div>
        ) : (
          <Button
            type="button"
            variant="ghost"
            size="sm"
            onClick={() => setShowDeleteConfirm(true)}
            className="h-8 px-3 text-sm font-medium text-red-500 hover:text-red-600 bg-red-50"
          >
            Delete
          </Button>
        )}
      </div>
    </div>
  );
}
