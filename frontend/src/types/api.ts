export interface ErrorResponse {
  code: string;
  message?: string;
}

export interface LoginResponse {
  access: string;
  is_email_verified: boolean;
}

export interface OAuthResponse {
  access: string;
  refresh: string;
}

export interface PaginationParams {
  page?: number;
  page_size?: number;
}

export interface BaseFiltersParams {
  search?: string;
  ordering?: string;
}

export interface ApiResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
