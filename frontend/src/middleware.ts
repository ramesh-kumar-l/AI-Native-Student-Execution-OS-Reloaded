import { NextResponse } from "next/server";
import { auth } from "@/auth";

export default auth((req) => {
  const { nextUrl } = req;
  const isLoggedIn = !!req.auth;

  const isAuthRoute = nextUrl.pathname.startsWith("/login") || nextUrl.pathname.startsWith("/register");
  const isDashboardRoute = nextUrl.pathname.startsWith("/dashboard");

  // Redirect authenticated users away from login/register to dashboard
  if (isAuthRoute && isLoggedIn) {
    return NextResponse.redirect(new URL("/dashboard", nextUrl));
  }

  // Redirect unauthenticated users to login
  if (isDashboardRoute && !isLoggedIn) {
    const callbackUrl = encodeURIComponent(nextUrl.pathname + nextUrl.search);
    return NextResponse.redirect(new URL(`/login?callbackUrl=${callbackUrl}`, nextUrl));
  }

  return NextResponse.next();
});

export const config = {
  matcher: [
    /*
     * Match all request paths except:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * - images, icons (if any)
     */
    "/((?!api|_next/static|_next/image|favicon.ico).*)",
  ],
};
