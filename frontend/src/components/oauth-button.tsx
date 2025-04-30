import { Button } from "~/components/ui/button";
import React from "react";
import { setPKCECookies } from "~/lib/pkce";
import { PROVIDERS } from "~/config/oauth";
import { env } from "~/env";
import { redirect } from "next/navigation";

interface OAuthButtonProps extends React.ComponentProps<typeof Button> {
  provider: keyof typeof PROVIDERS;
}

export default async function OAuthButton({
  children,
  provider,
  ...props
}: OAuthButtonProps) {
  const handleLogin = async () => {
    "use server";

    const { code_challenge, state } = await setPKCECookies(provider);
    const redirectUrl = new URL(PROVIDERS[provider].auth_url);

    redirectUrl.searchParams.set("client_id", PROVIDERS[provider].client_id);
    redirectUrl.searchParams.set(
      "redirect_uri",
      `${env.NEXT_PUBLIC_APP_URL}/api/oauth`,
    );
    redirectUrl.searchParams.set("response_type", "code");
    redirectUrl.searchParams.set("scope", PROVIDERS[provider].scopes);
    redirectUrl.searchParams.set("code_challenge", code_challenge);
    redirectUrl.searchParams.set("code_challenge_method", "S256");
    redirectUrl.searchParams.set("state", `${provider}:${state}`);
    redirectUrl.searchParams.set(
      "optional_scope",
      PROVIDERS[provider].optional_scopes ?? "",
    );

    return redirect(redirectUrl.toString());
  };

  return (
    <form action={handleLogin} className="flex-1">
      <Button type="submit" className="w-full" variant="secondary" {...props}>
        {children}
      </Button>
    </form>
  );
}
