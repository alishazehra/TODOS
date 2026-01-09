import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { email, password, confirm_password } = body;

    if (!email || !password || !confirm_password) {
      return NextResponse.json(
        { detail: "Email, password, and confirm_password are required" },
        { status: 400 }
      );
    }

    if (password !== confirm_password) {
      return NextResponse.json(
        { detail: "Passwords do not match" },
        { status: 400 }
      );
    }

    if (password.length < 8) {
      return NextResponse.json(
        { detail: "Password must be at least 8 characters" },
        { status: 400 }
      );
    }

    const response = await fetch(
      "https://todos-1-yq2e.onrender.com/api/v1/auth/signup",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, confirm_password }),
      }
    );

    const data = await response.json();

    if (!response.ok) {
      // Handle different error formats from backend
      let errorMsg = "Signup failed";
      if (data?.detail?.error?.message) {
        errorMsg = data.detail.error.message;
      } else if (typeof data?.detail === "string") {
        errorMsg = data.detail;
      } else if (typeof data?.detail === "object") {
        errorMsg = JSON.stringify(data.detail);
      }
      return NextResponse.json(
        { detail: errorMsg },
        { status: response.status }
      );
    }

    return NextResponse.json(data);
  } catch (error) {
    return NextResponse.json(
      { detail: "Internal server error" },
      { status: 500 }
    );
  }
}
