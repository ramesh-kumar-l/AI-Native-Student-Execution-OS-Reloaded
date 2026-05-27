const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

export interface ApiResponse<T = any> {
  data: T | null;
  error: string | null;
}

export async function apiFetch<T = any>(
  path: string,
  options: RequestInit = {},
  token?: string
): Promise<ApiResponse<T>> {
  const url = `${BACKEND_URL}${path}`;
  const headers = new Headers(options.headers || {});

  if (!headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  try {
    const response = await fetch(url, {
      ...options,
      headers,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      return {
        data: null,
        error: errorData.detail || `HTTP error! Status: ${response.status}`,
      };
    }

    const data = await response.json();
    return { data, error: null };
  } catch (err: any) {
    console.error(`Fetch failed at ${url}:`, err);
    return { data: null, error: err.message || "Network request failed" };
  }
}
