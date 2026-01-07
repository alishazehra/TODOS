"use client";

import { useEffect, useState, useCallback } from "react";
import { TodoList } from "@/components/TodoList";
import { api } from "@/lib/api";
import { Todo } from "@/types";

export const dynamic = 'force-dynamic';

export default function TodosPage() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  const loadTodos = useCallback(async () => {
    try {
      const response = await api.getTodos();
      setTodos(response.todos);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load todos");
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    loadTodos();
  }, [loadTodos]);

  const handleToggle = async (todo: Todo) => {
    if (!todo?.id) return;
    try {
      const response = await api.toggleTodo(todo.id);
      setTodos((prev) =>
        prev.map((t) => (t.id === todo.id ? response : t))
      );
    } catch (err) {
      console.error("Failed to toggle todo:", err);
    }
  };

  const handleDelete = async (todo: Todo) => {
    if (!todo?.id) return;
    try {
      await api.deleteTodo(todo.id);
      setTodos((prev) => prev.filter((t) => t.id !== todo.id));
    } catch (err) {
      console.error("Failed to delete todo:", err);
    }
  };

  const handleUpdate = async (todo: Todo, description: string) => {
    if (!todo?.id) return;
    try {
      const response = await api.updateTodo(todo.id, { description });
      setTodos((prev) =>
        prev.map((t) => (t.id === todo.id ? response : t))
      );
    } catch (err) {
      console.error("Failed to update todo:", err);
    }
  };

  const handleAdd = (todo: Todo) => {
    if (todo && todo.id) {
      setTodos((prev) => [todo, ...prev]);
    }
  };

  if (error) {
    return (
      <div className="text-center py-12">
        <div className="p-3 text-sm text-red-500 bg-red-50 border border-red-200 rounded-lg inline-block">
          {error}
        </div>
      </div>
    );
  }

  return (
    <TodoList
      todos={todos}
      isLoading={isLoading}
      onToggle={handleToggle}
      onDelete={handleDelete}
      onUpdate={handleUpdate}
      onAdd={handleAdd}
    />
  );
}
