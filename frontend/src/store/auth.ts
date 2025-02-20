import { create } from "zustand";
import { persist } from "zustand/middleware";

type AuthState = {
  accessToken: string | null;
  setAccessToken: (token: string | null) => void;
  logout: () => void;
};

export const useAuthStore = create(
  persist<AuthState>(
    (set, get) => ({
      accessToken: null,
      setAccessToken: (token: string | null) => set({ accessToken: token }),
      logout: () => set({ accessToken: null }),
    }),
    { name: "auth-storage" },
  ),
);
