export async function POST(req: Request) {
  const body = await req.json();

  const response = await fetch(
    "https://todos-1-yq2e.onrender.com/api/v1/auth/signup",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    }
  );

  const data = await response.json();

  return new Response(JSON.stringify(data), {
    status: response.status,
    headers: { "Content-Type": "application/json" },
  });
}
