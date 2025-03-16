import { LoginForm } from "~/components/forms/login";
import { YandexLoginButton } from "~/components/yandex-login-button";
import { Suspense } from "react";

export default function LoginPage() {
  return (
    <>
      <Suspense>
        <LoginForm />
      </Suspense>
      <div className="after:border-border relative my-4 text-center text-sm after:absolute after:inset-0 after:top-1/2 after:z-0 after:flex after:items-center after:border-t">
        <span className="bg-background text-muted-foreground relative z-10 px-2">
          или
        </span>
      </div>
      <YandexLoginButton />
    </>
  );
}
