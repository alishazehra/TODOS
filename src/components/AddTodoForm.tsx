"use client";

import { useState } from "react";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { api } from "@/lib/api";
import { Todo } from "@/types";

interface AddTodoFormProps {
  onTodoAdded: (todo: Todo) => void;
}

export function AddTodoForm({ onTodoAdded }: AddTodoFormProps) {
  const [description, setDescription] = useState("");
  
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    if (!description.trim()) {
      setError("Please enter a todo");
      return;
    }

    setIsLoading(true);
    try {
      const response = await api.createTodo({ description });
      onTodoAdded(response);
      setDescription("");
      
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to add todo");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
  <div className="flex-1">



        <Input
  placeholder="What needs to be done?"
  value={description}
  onChange={(e) => setDescription(e.target.value)}
  error={error}
  className="w-full max-w-3xl h-14 px-3"
 />

      
     
      
</div>
      <Button type="submit" isLoading={isLoading}>
        Add
      </Button>
    </form>
  );
} 