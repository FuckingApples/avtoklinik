import { type NextRequest, NextResponse } from "next/server";

export function middleware(req: NextRequest) {
  const refreshCookie = req.cookies.get("refresh")?.value;

  if (!refreshCookie) {
    return NextResponse.redirect(
      new URL(`/login?redirect=${req.nextUrl.pathname}`, req.url),
    );
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*"],
};
