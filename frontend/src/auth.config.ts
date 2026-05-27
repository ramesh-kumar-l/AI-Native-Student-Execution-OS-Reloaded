import type { NextAuthConfig } from "next-auth";
import Google from "next-auth/providers/google";
import Credentials from "next-auth/providers/credentials";

export default {
  providers: [
    Google({
      clientId: process.env.AUTH_GOOGLE_ID,
      clientSecret: process.env.AUTH_GOOGLE_SECRET,
    }),
    Credentials({
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;

        const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";
        try {
          const res = await fetch(`${backendUrl}/api/v1/auth/login`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              email: credentials.email,
              password: credentials.password,
            }),
          });

          if (!res.ok) {
            const errData = await res.json().catch(() => ({}));
            throw new Error(errData.detail || "Authentication failed");
          }

          const tokens = await res.json();
          if (tokens.access_token) {
            // Return user object containing the JWT token payload. NextAuth stores this user inside token/session.
            return {
              id: "credentials-user", // dummy ID required by NextAuth user schema
              email: credentials.email as string,
              accessToken: tokens.access_token,
              refreshToken: tokens.refresh_token,
            };
          }
        } catch (error) {
          console.error("Auth authorization error:", error);
        }
        return null;
      },
    }),
  ],
} satisfies NextAuthConfig;
