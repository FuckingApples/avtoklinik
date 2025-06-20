import { type NextRequest, NextResponse } from "next/server";
import { PROVIDERS } from "~/config/oauth";
import { cookies } from "next/headers";
import axios from "axios";
import { env } from "~/env";
import type { OAuthResponse } from "~/types/api";

export async function GET(req: NextRequest) {
  const cookieStorage = await cookies();
  const { searchParams, origin, pathname } = new URL(req.url);
  const code = searchParams.get("code");
  const state = searchParams.get("state");

  if (!code || !state) {
    return NextResponse.json("Missing required parameters", { status: 400 });
  }

  const [provider, stateValue] = state.split("_") as [
    keyof typeof PROVIDERS,
    string,
  ];

  if (!PROVIDERS[provider]) {
    return NextResponse.json("Invalid provider", { status: 400 });
  }

  const storedState = cookieStorage.get(`oauth_state_${provider}`)?.value;
  if (stateValue !== storedState) {
    return NextResponse.json("Invalid state", { status: 400 });
  }

  const code_verifier = cookieStorage.get(`pkce_${provider}`)?.value;

  const requestBody: Record<string, string> = {
    code,
    redirect_uri: origin + pathname,
    ...(code_verifier && { code_verifier }),
  };

  const allParams = Object.fromEntries(searchParams.entries());
  const allowedParams = [
    ...PROVIDERS[provider].required_params,
    ...PROVIDERS[provider].optional_params,
  ];

  for (const [key, value] of Object.entries(allParams)) {
    if (allowedParams.includes(key) && !requestBody[key]) {
      requestBody[key] = value;
    }
  }

  try {
    const backendResponse = await axios.post<OAuthResponse>(
      `${env.NEXT_PUBLIC_API_URL}/v1/oauth/${provider}/`,
      requestBody,
      {
        withCredentials: true,
      },
    );

    const response = NextResponse.redirect(new URL("/dashboard", req.url));

    if (backendResponse.headers["set-cookie"]) {
      backendResponse.headers["set-cookie"].forEach((cookie) => {
        response.headers.append("Set-Cookie", cookie);
      });
    }
    return response;
  } catch (error) {
    console.error(error);
    return NextResponse.json("Authentication failed", { status: 500 });
  }
}
