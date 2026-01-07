"use client";

import { Todo } from "@/types";
import { TodoItem } from "./TodoItem";
import { AddTodoForm } from "./AddTodoForm";
import { Spinner } from "@/components/ui/Spinner";

interface TodoListProps {
  todos: Todo[];
  isLoading: boolean;
  onToggle: (todo: Todo) => void;
  onDelete: (todo: Todo) => void;
  onUpdate: (todo: Todo, description: string) => void;
  onAdd: (todo: Todo) => void;
}

export function TodoList({
  todos,
  isLoading,
  onToggle,
  onDelete,
  onUpdate,
  onAdd,
}: TodoListProps) {
  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <Spinner size="lg" />
      </div>
    );
  }

  const activeTodos = todos.filter(t => t && t.id && !t.completed);
  const completedTodos = todos.filter(t => t && t.id && t.completed);

  return (
    <div className="space-y-6">
      <AddTodoForm onTodoAdded={onAdd} />

      {todos.length === 0 ? (
        <div className="text-center py-12">
          <div className="text-4xl mb-4">📝</div>
          <h3 className="text-lg font-medium text-foreground mb-2">
            No todos yet
          </h3>
          <p className="text-muted-foreground">
            Add your first todo above to get started!
          </p>
        </div>
      ) : (
        <div className="space-y-8">
          {/* Active Todos Section */}
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <h2 className="text-lg font-semibold text-foreground">Active Todos</h2>
              <span className="text-sm text-muted-foreground">({activeTodos.length})</span>
            </div>
            {activeTodos.length === 0 ? (
              <div className="text-center py-8 bg-muted/30 rounded-lg border-2 border-dashed border-muted">
                <p className="text-sm text-muted-foreground">No active todos</p>
              </div>
            ) : (
              activeTodos.map((todo) => (
                <TodoItem
                  key={todo.id}
                  todo={todo}
                  onToggle={onToggle}
                  onDelete={onDelete}
                  onUpdate={onUpdate}
                />
              ))
            )}
          </div>

          {/* Completed Todos Section */}
          {completedTodos.length > 0 && (
            <div className="space-y-3">
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-semibold text-foreground">Completed</h2>
                <span className="text-sm text-muted-foreground">({completedTodos.length})</span>
              </div>
              <div className="bg-muted/20 rounded-lg border border-muted-foreground/20 p-4 space-y-3">
                {completedTodos.map((todo) => (
                  <TodoItem
                    key={todo.id}
                    todo={todo}
                    onToggle={onToggle}
                    onDelete={onDelete}
                    onUpdate={onUpdate}
                  />
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
