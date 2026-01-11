"use client";
import { useState, useEffect, useRef } from "react";

export function useAuth() {
  const [user, setUser] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const initialized = useRef(false);

  // Initialize user from localStorage on mount
  useEffect(() => {
    if (typeof window !== "undefined" && !initialized.current) {
      initialized.current = true;
      const userInfo = localStorage.getItem("user_info");
      if (userInfo) {
        try {
          setUser(JSON.parse(userInfo));
        } catch (e) {
          console.error("Failed to parse user info", e);
        }
      }
      setIsLoading(false);
    }
  }, []);

  const isAuthenticated = !!user;

  const signup = async (email: string, password: string, confirm_password: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'https://todos-1-yq2e.onrender.com';
      const res = await fetch(`${apiUrl}/api/v1/auth/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, confirm_password }),
      });
      const data = await res.json();
      if (!res.ok) {
        let errorMsg = "Signup failed";
        if (data?.detail?.error?.message) {
          errorMsg = data.detail.error.message;
        } else if (typeof data?.detail === "string") {
          errorMsg = data.detail;
        } else if (typeof data?.detail === "object") {
          errorMsg = JSON.stringify(data.detail);
        }
        throw new Error(errorMsg);
      }
      setUser(data.user);
      localStorage.setItem("user_info", JSON.stringify(data.user));
      localStorage.setItem("session_token", data.session.token);
      return data;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Signup failed");
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  const signin = async (email: string, password: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_BASE_URL || 'https://todos-1-yq2e.onrender.com';
      const res = await fetch(`${apiUrl}/api/v1/auth/signin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (!res.ok) {
        let errorMsg = "Signin failed";
        if (data?.detail?.error?.message) {
          errorMsg = data.detail.error.message;
        } else if (data?.error?.message) {
          errorMsg = data.error.message;
        } else if (typeof data?.detail === "string") {
          errorMsg = data.detail;
        } else if (typeof data?.detail === "object") {
          errorMsg = JSON.stringify(data.detail);
        }
        throw new Error(errorMsg);
      }
      setUser(data.user);
      localStorage.setItem("user_info", JSON.stringify(data.user));
      localStorage.setItem("session_token", data.session.token);
      return data;
    } catch (err) {
      const msg = err instanceof Error ? err.message : "Signin failed";
      setError(msg);
      throw new Error(msg);
    } finally {
      setIsLoading(false);
    }
  };

  const signout = () => {
    setUser(null);
    localStorage.removeItem("session_token");
    localStorage.removeItem("user_info");
  };

  return { user, isAuthenticated, error, isLoading, signup, signin, signout };
}
