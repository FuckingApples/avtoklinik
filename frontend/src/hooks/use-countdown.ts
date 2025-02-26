import { useTimerStore } from "~/store/timer";
import { useEffect, useState } from "react";

export const useCountdown = () => {
  const { endTime, isCooldown, clearTimer } = useTimerStore();
  const [timeLeft, setTimeLeft] = useState<number>(0);

  useEffect(() => {
    if (!endTime) return;

    const timer = setInterval(() => {
      const now = Date.now();
      const difference = endTime - now;
      const secondsLeft = Math.floor(difference / 1000);

      if (secondsLeft <= 0) {
        clearTimer();
        clearInterval(timer);
        setTimeLeft(0);
      } else {
        setTimeLeft(secondsLeft);
      }
    }, 1000);

    return () => clearInterval(timer);
  }, [endTime]);

  const formatTime = (secs: number) => {
    const minutes = Math.floor(secs / 60);
    const seconds = secs % 60;
    return { minutes, seconds };
  };

  return { formatedTime: formatTime(timeLeft), isCooldown, timeLeft };
};
