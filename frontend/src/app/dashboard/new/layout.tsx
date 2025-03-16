import React, { Suspense } from "react";

export default function NewOrganizationLayout({
  children,
}: React.PropsWithChildren) {
  return <Suspense>{children}</Suspense>;
}
