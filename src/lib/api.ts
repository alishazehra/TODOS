import axios, { AxiosError, AxiosInstance, AxiosResponse } from "axios";
import type {
  SignupRequest,
  SigninRequest,
  CreateTodoRequest,
  UpdateTodoRequest,
  AuthResponse,
  TodoListResponse,
  TodoResponse,
  UserResponse,
  ErrorResponse,
} from "@/types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "https://todos-1-yq2e.onrender.com";

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: `${API_URL}/api/v1`,
      withCredentials: true,
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Request interceptor
    this.client.interceptors.request.use(
      (config) => {
        // Get token from localStorage (only available in browser)
        if (typeof window !== "undefined") {
          const token = localStorage.getItem("session_token");
          if (token) {
            config.headers.Authorization = `Bearer ${token}`;
          }
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    // Response interceptor
    this.client.interceptors.response.use(
      (response) => response,
      (error: AxiosError<ErrorResponse>) => {
        if (error.response?.status === 401) {
          // Clear session and redirect to signin (only in browser)
          if (typeof window !== "undefined") {
            localStorage.removeItem("session_token");
            window.location.href = "/signin";
          }
        }
        return Promise.reject(error);
      }
    );
  }

  // Auth endpoints
  async signup(data: SignupRequest): Promise<AuthResponse> {
    const response: AxiosResponse<AuthResponse> = await this.client.post(
      "/auth/signup",
      data
    );
    return response.data;
  }

  async signin(data: SigninRequest): Promise<AuthResponse> {
    const response: AxiosResponse<AuthResponse> = await this.client.post(
      "/auth/signin",
      data
    );
    return response.data;
  }

  async signout(): Promise<void> {
    await this.client.post("/auth/signout");
  }

  async getCurrentUser(): Promise<UserResponse> {
    const response: AxiosResponse<UserResponse> = await this.client.get(
      "/auth/me"
    );
    return response.data;
  }

  // Todo endpoints
  async getTodos(): Promise<TodoListResponse> {
    const response: AxiosResponse<TodoListResponse> = await this.client.get(
      "/todos"
    );
    return response.data;
  }

  async createTodo(data: CreateTodoRequest): Promise<TodoResponse> {
    const response: AxiosResponse<TodoResponse> = await this.client.post(
      "/todos",
      data
    );
    return response.data;
  }

  async getTodo(id: string): Promise<TodoResponse> {
    const response: AxiosResponse<TodoResponse> = await this.client.get(
      `/todos/${id}`
    );
    return response.data;
  }

  async updateTodo(id: string, data: UpdateTodoRequest): Promise<TodoResponse> {
    const response: AxiosResponse<TodoResponse> = await this.client.put(
      `/todos/${id}`,
      data
    );
    return response.data;
  }

  async deleteTodo(id: string): Promise<void> {
    await this.client.delete(`/todos/${id}`);
  }

  async toggleTodo(id: string): Promise<TodoResponse> {
    const response: AxiosResponse<TodoResponse> = await this.client.patch(
      `/todos/${id}/toggle`
    );
    return response.data;
  }
}

export const api = new ApiClient();
