"use client";

import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import { useRouter } from "next/navigation";
import { User, AuthResponse } from "@/types";
import { api } from "./api";

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  signin: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string, confirmPassword: string) => Promise<void>;
  signout: () => Promise<void>;
  error: string | null;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  // Check for existing session on mount
  useEffect(() => {
    const checkSession = async () => {
      // Only access localStorage in browser
      if (typeof window !== "undefined") {
        const token = localStorage.getItem("session_token");
        if (token) {
          try {
            const response = await api.getCurrentUser();
            setUser(response);
          } catch {
            localStorage.removeItem("session_token");
          }
        }
      }
      setIsLoading(false);
    };
    checkSession();
  }, []);

  const signin = async (email: string, password: string) => {
    setError(null);
    setIsLoading(true);
    try {
      const response = await api.signin({ email, password });
      localStorage.setItem("session_token", response.session.token);
      setUser(response.user);
      router.push("/todos");
    } catch (err: unknown) {
      const axiosError = err as { response?: { data?: { error?: { message?: string } } } };
      const message = axiosError.response?.data?.error?.message || "Sign in failed";
      setError(message);
      throw new Error(message);
    } finally {
      setIsLoading(false);
    }
  };

  const signup = async (email: string, password: string, confirmPassword: string) => {
    setError(null);
    setIsLoading(true);
    try {
      const response = await api.signup({ email, password, confirm_password: confirmPassword });
      localStorage.setItem("session_token", response.session.token);
      setUser(response.user);
      router.push("/todos");
    } catch (err: unknown) {
      const axiosError = err as { response?: { data?: { error?: { message?: string } } } };
      const message = axiosError.response?.data?.error?.message || "Sign up failed";
      setError(message);
      throw new Error(message);
    } finally {
      setIsLoading(false);
    }
  };

  const signout = async () => {
    try {
      await api.signout();
    } catch {
      // Ignore signout errors
    } finally {
      localStorage.removeItem("session_token");
      setUser(null);
      router.push("/signin");
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: !!user,
        isLoading,
        signin,
        signup,
        signout,
        error,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
