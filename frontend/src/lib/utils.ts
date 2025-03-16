import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]): string {
  return twMerge(clsx(inputs));
}

// Функция для генерации хеша из строки
function hashCode(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }
  return hash;
}

// Функция для преобразования числа в HEX-цвет
function generateHSL(
  hash: number,
  saturation: number,
  lightness: number,
): string {
  const hue = Math.abs(hash) % 360;
  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}

// Генерация палитры из 3 гармоничных цветов
const generateColorPalette = (str: string) => {
  const baseHash = hashCode(str);

  return [
    generateHSL(baseHash, 70, 40), // Основной цвет
    generateHSL(baseHash + 30, 80, 50), // Смещенный на 30 градусов
    generateHSL(baseHash - 30, 60, 60), // Смещенный в другую сторону
  ];
};

// Генерации градиента
export function generateSmoothGradient(str: string, deg = 135): string {
  if (!str) return "";

  const colors = generateColorPalette(str);
  return `
    linear-gradient(
      ${deg}deg,
      ${colors[0]} 0%,
      ${colors[1]} 50%,
      ${colors[2]} 100%
    )
  `;
}

export function getInitials(str: string): string {
  return str
    .split(" ")
    .map((p) => p[0])
    .join("")
    .toUpperCase();
}
