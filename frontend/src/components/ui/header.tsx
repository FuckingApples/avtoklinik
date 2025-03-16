import Link from "next/link";
import { CarFront } from "lucide-react";
import { env } from "~/env";
import React from "react";
import UserSpaceNav from "~/components/user-space-nav";

function Header() {
  return (
    <header className="border-b-border flex h-12 flex-row items-center border px-4">
      <div className="flex justify-center md:justify-start">
        <Link href="/" className="flex items-center gap-2 font-medium">
          <div className="bg-primary text-primary-foreground flex h-6 w-6 items-center justify-center rounded-md">
            <CarFront className="size-4" />
          </div>
          {env.NEXT_PUBLIC_APP_NAME}
        </Link>
      </div>
      <div className="ml-auto">
        <UserSpaceNav side="right">adasd</UserSpaceNav>
      </div>
    </header>
  );
}

export default Header;
