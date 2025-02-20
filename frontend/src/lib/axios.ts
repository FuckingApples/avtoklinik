import axios, { type AxiosError, type InternalAxiosRequestConfig } from "axios";
import { env } from "~/env";
import { useAuthStore } from "~/store/auth";

const api = axios.create({
  baseURL: env.NEXT_PUBLIC_API_URL,
  withCredentials: true,
});

api.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().accessToken;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error: AxiosError) => Promise.reject(error),
);

api.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config as InternalAxiosRequestConfig & {
      _retry?: boolean;
    };

    if (error.response?.status === 401 && !originalRequest?._retry) {
      originalRequest._retry = true;

      try {
        const { data }: { data: { access: string } } = await axios.post(
          `${env.NEXT_PUBLIC_API_URL}/token/refresh`,
          {},
          { withCredentials: true },
        );

        useAuthStore.getState().setAccessToken(data.access);
        originalRequest.headers.Authorization = `Bearer ${data.access}`;

        return api(originalRequest);
      } catch (refreshError) {
        useAuthStore.getState().logout();

        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  },
);

export default api;
