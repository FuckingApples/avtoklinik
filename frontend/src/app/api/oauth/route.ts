import { type NextRequest, NextResponse } from "next/server";
import type { PROVIDERS } from "~/config/oauth";
import { cookies } from "next/headers";
import axios from "axios";
import { env } from "~/env";
import type { OAuthResponse } from "~/types/api";

export async function GET(req: NextRequest) {
  const cookieStorage = await cookies();
  const { searchParams } = new URL(req.url);
  const code = searchParams.get("code");
  const state = searchParams.get("state");

  if (!code || !state)
    return NextResponse.json("Missing required parameters", { status: 400 });

  const [provider, stateValue] = state.split(":") as [
    keyof typeof PROVIDERS,
    string,
  ];
  const storedState = cookieStorage.get(`oauth_state_${provider}`)?.value;

  if (stateValue !== storedState) {
    return NextResponse.json("Invalid state", { status: 400 });
  }

  const code_verifier = cookieStorage.get(`pkce_${provider}`)?.value;

  const backendResponse = await axios.post<OAuthResponse>(
    `${env.NEXT_PUBLIC_API_URL}/v1/oauth/${provider}/`,
    { code, code_verifier },
    {
      withCredentials: true,
    },
  );

  const response = NextResponse.redirect(new URL("/dashboard", req.url));
  const setCookieHeader = backendResponse.headers["set-cookie"];
  if (setCookieHeader) {
    setCookieHeader.forEach((cookie) => {
      response.headers.append("Set-Cookie", cookie);
    });
  }

  return response;
}
