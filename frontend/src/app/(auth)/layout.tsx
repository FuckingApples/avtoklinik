import React from "react";
import Image from "next/image";
import Link from "next/link";
import { CarFront } from "lucide-react";
import { env } from "~/env";

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
          className="absolute inset-0 h-full w-full rounded-lg object-cover dark:brightness-[0.2] dark:grayscale"
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
          <div className="w-full max-w-xs">{children}</div>
        </div>
      </div>
    </div>
  );
}
