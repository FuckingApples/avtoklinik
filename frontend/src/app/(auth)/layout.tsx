import React from "react";
import Image from "next/image";
import Link from "next/link";
import { CarFront, KeyRoundIcon } from "lucide-react";
import { env } from "~/env";
import OAuthButton from "~/components/oauth-button";

export default function AuthLayout({
  children,
}: Readonly<React.PropsWithChildren>) {
  return (
    <div className="grid min-h-svh p-2 lg:grid-cols-2">
      <div className="bg-muted relative hidden rounded-lg lg:block">
        <Image
          width={0} // Width & height will be ignored, but they are required
          height={0}
          src="/placeholder.svg"
          alt="Placeholder"
          className="absolute inset-0 h-full w-full rounded-lg object-cover dark:brightness-[0.8]"
        />
      </div>
      <div className="flex flex-col gap-4 p-6 md:p-10">
        <div className="flex justify-center md:justify-start">
          <Link href="/" className="flex items-center gap-2 font-medium">
            <div className="bg-primary text-primary-foreground flex h-6 w-6 items-center justify-center rounded-md">
              <CarFront className="size-4" />
            </div>
            {env.NEXT_PUBLIC_APP_NAME}
          </Link>
        </div>
        <div className="flex flex-1 items-center justify-center">
          <div className="relative w-full max-w-xs">
            {children}
            <div className="after:border-border relative my-4 text-center text-sm after:absolute after:inset-0 after:top-1/2 after:z-0 after:flex after:items-center after:border-t">
              <span className="bg-background text-muted-foreground relative z-10 px-2">
                или
              </span>
            </div>
            <div className="flex flex-wrap gap-2">
              {/*<OAuthButton className="font-semibold">*/}
              {/*  <KeyRoundIcon /> Passkey*/}
              {/*</OAuthButton>*/}
              <OAuthButton provider="yandex">
                <Image
                  src="providers/yandex.svg"
                  alt="Войти через Яндекс"
                  className="size-6 rounded-full"
                  width={0}
                  height={0}
                />
              </OAuthButton>
              <OAuthButton provider="vk">
                <Image
                  src="providers/vk.svg"
                  alt="Войти через VK"
                  className="size-6"
                  width={0}
                  height={0}
                />
              </OAuthButton>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
