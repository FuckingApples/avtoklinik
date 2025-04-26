import React from "react";
import Header from "~/components/ui/header";

export default function UserSpaceLayout({ children }: React.PropsWithChildren) {
  return (
    <>
      <Header></Header>
      {children}
    </>
  );
}
