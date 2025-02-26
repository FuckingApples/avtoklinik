import { create } from "zustand";
import { persist } from "zustand/middleware";

type TimerState = {
  endTime: number | null;
  isCooldown: boolean;
  startTimer: (minutes: number) => void;
  clearTimer: () => void;
};

const timerPersist = persist<TimerState>(
  (set) => ({
    endTime: null,
    isCooldown: false,
    startTimer: (minutes: number) => {
      const endTime = Date.now() + minutes * 60 * 1000;
      set({ endTime, isCooldown: true });
    },
    clearTimer: () => set({ endTime: null, isCooldown: false }),
  }),
  { name: "timer-storage" },
);

export const useTimerStore = create<TimerState>()(timerPersist);
