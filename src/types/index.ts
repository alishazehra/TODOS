// User types
export interface User {
  id: string;
  email: string;
  createdAt: string;
  updatedAt: string;
}

// Todo types
export interface Todo {
  id: string;
  userId: string;
  description: string;
  completed: boolean;
  createdAt: string;
  updatedAt: string;
}

// API Request types
export interface SignupRequest {
  email: string;
  password: string;
  confirm_password: string;
}

export interface SigninRequest {
  email: string;
  password: string;
}

export interface CreateTodoRequest {
  description: string;
}

export interface UpdateTodoRequest {
  description?: string;
  completed?: boolean;
}

// API Response types
export interface AuthResponse {
  user: User;
  session: {
    token: string;
    expiresAt: string;
  };
}

export interface TodoListResponse {
  todos: Todo[];
}

// API returns todo directly, not wrapped in {todo: ...}
export interface TodoResponse {
  id: string;
  userId: string;
  description: string;
  completed: boolean;
  createdAt: string;
  updatedAt: string;
}

// UserResponse is the user directly (not wrapped)
export type UserResponse = User;

export interface ErrorResponse {
  error: {
    code: string;
    message: string;
    details?: Record<string, string[]>;
  };
}

// Form state types
export interface FormState {
  isLoading: boolean;
  error: string | null;
  success: string | null;
}
