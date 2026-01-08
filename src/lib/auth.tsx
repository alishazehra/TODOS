
  "use client";

import { useState } from "react";

export const useAuth = () => {
  const [user, setUser] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  // Signup function
  const signup = async (email: string, password: string, confirmPassword: string) => {
    setError(null);

    if (password !== confirmPassword) {
      throw new Error("Passwords do not match");
    }

    if (password.length < 8) {
      throw new Error("Password must be at least 8 characters");
    }

    try {
      const response = await fetch(`${apiUrl}/api/v1/auth/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Signup failed");
      }

      const data = await response.json();
      setUser(data.user || null);
      return data;
    } catch (err: any) {
      setError(err.message || "Signup failed");
      throw err;
    }
  };

  // Signin function
  const signin = async (email: string, password: string) => {
    setError(null);

    try {
      const response = await fetch(`${apiUrl}/api/v1/auth/signin`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Signin failed");
      }

      const data = await response.json();
      setUser(data.user || null);
      return data;
    } catch (err: any) {
      setError(err.message || "Signin failed");
      throw err;
    }
  };

  return {
    user,
    error,
    signup,
    signin,
  };
};
