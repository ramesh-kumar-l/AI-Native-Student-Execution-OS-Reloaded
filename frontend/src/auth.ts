import NextAuth from "next-auth";
import authConfig from "./auth.config";

export const { handlers, auth, signIn, signOut } = NextAuth({
  session: { strategy: "jwt" },
  pages: {
    signIn: "/login",
  },
  callbacks: {
    async jwt({ token, user, account }) {
      // 1. Initial Credentials Sign In
      if (user && !account) {
        token.accessToken = (user as any).accessToken;
        token.refreshToken = (user as any).refreshToken;
        token.email = user.email;
      }
      
      // 2. Google OAuth Sign In
      if (account && account.provider === "google") {
        const idToken = account.id_token;
        const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";
        
        try {
          // Synchronize/Register Google OAuth account with the FastAPI backend
          const res = await fetch(`${backendUrl}/api/v1/auth/google`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              id_token: idToken,
            }),
          });
          
          if (res.ok) {
            const tokens = await res.json();
            token.accessToken = tokens.access_token;
            token.refreshToken = tokens.refresh_token;
          } else {
            console.error("Failed to sync Google user with backend api:", await res.text());
          }
        } catch (e) {
          console.error("Google OAuth token exchange error:", e);
        }
      }
      
      return token;
    },
    async session({ session, token }) {
      if (token) {
        session.accessToken = token.accessToken as string;
        session.refreshToken = token.refreshToken as string;
      }
      return session;
    },
  },
  ...authConfig,
});
