import { create } from "zustand";
import { persist } from "zustand/middleware";

type AuthState = {
  accessToken: string | null;
  setAccessToken: (token: string | null) => void;
  logout: () => void;
};

const authPersist = persist<AuthState>(
  (set) => ({
    accessToken: null,
    setAccessToken: (token: string | null) => set({ accessToken: token }),
    logout: () => set({ accessToken: null }),
  }),
  { name: "auth-storage" },
);

export const useAuthStore = create<AuthState>()(authPersist);
