import { RegistrationForm } from "~/components/forms/registration";
import { YandexLoginButton } from "~/components/yandex-login-button";

export default function RegisterPage() {
  return (
    <>
      <RegistrationForm />
      <div className="after:border-border relative my-4 text-center text-sm after:absolute after:inset-0 after:top-1/2 after:z-0 after:flex after:items-center after:border-t">
        <span className="bg-background text-muted-foreground relative z-10 px-2">
          или
        </span>
      </div>
      <YandexLoginButton />
    </>
  );
}
