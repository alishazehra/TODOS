// src/app/api/signup/route.ts
export async function POST(req: Request) {
  try {
    const body = await req.json();

    const response = await fetch(
      "https://todos-1-yq2e.onrender.com/api/v1/auth/signup",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      }
    );

    let data: any;
    try {
      data = await response.json();
    } catch {
      data = {};
    }

    if (!response.ok) {
      // Make sure detail is always a string
      const errorMessage =
        typeof data.detail === "string"
          ? data.detail
          : typeof data.message === "string"
          ? data.message
          : "Signup failed";
      return new Response(JSON.stringify({ detail: errorMessage }), {
        status: response.status,
        headers: { "Content-Type": "application/json" },
      });
    }

    return new Response(JSON.stringify(data), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  } catch (err) {
    return new Response(JSON.stringify({ detail: "Internal server error" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}
