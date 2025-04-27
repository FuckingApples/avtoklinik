"use server";

import {
  generateCodeChallenge,
  generateCodeVerifier,
  generateState,
} from "~/utils/pkce";
import { cookies } from "next/headers";
import { env } from "~/env";

export async function setPKCECookies(provider: string) {
  const cookieStore = await cookies();
  const state = generateState();
  const code_verifier = generateCodeVerifier();
  const code_challenge = await generateCodeChallenge(code_verifier);

  cookieStore.set(`pkce_${provider}`, code_verifier, {
    httpOnly: true,
    secure: env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: 600,
    path: "/api/oauth",
  });
  cookieStore.set(`oauth_state_${provider}`, state, {
    httpOnly: true,
    secure: env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: 600,
    path: "/api/oauth",
  });

  return { code_challenge, state };
}
