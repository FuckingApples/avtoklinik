export type ErrorResponse = {
  code: string;
  message?: string;
};

export type LoginResponse = {
  access: string;
  is_email_verified: boolean;
};

export type OAuthResponse = {
  access: string;
  refresh: string;
};
