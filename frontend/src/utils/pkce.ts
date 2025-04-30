function generateRandomString(length: number): string {
  const arr = new Uint8Array(length);
  crypto.getRandomValues(arr);
  return Array.from(arr, (dec) => ("0" + dec.toString(16)).substring(-2)).join(
    "",
  );
}

export function generateCodeVerifier() {
  return generateRandomString(64);
}

export function generateState() {
  return generateRandomString(32);
}

export async function generateCodeChallenge(codeVerifier: string) {
  const encoder = new TextEncoder();
  const data = encoder.encode(codeVerifier);
  const digest = await crypto.subtle.digest("SHA-256", data);

  return btoa(String.fromCharCode(...new Uint8Array(digest)))
    .replace(/\+/g, "-")
    .replace(/\//g, "_")
    .replace(/=+$/, "");
}
