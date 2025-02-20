import { type NextRequest, NextResponse } from "next/server";

export function middleware(req: NextRequest) {
  const refreshCookie = req.cookies.get("refresh")?.value;

  const loginRoutes = ["/login", "/register"];

  if (!loginRoutes.includes(req.nextUrl.pathname) && !refreshCookie) {
    return NextResponse.redirect(new URL("/login", req.url));
  }

  if (loginRoutes.includes(req.nextUrl.pathname) && refreshCookie) {
    return NextResponse.redirect(new URL("/dashboard", req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/login", "/register"],
};
