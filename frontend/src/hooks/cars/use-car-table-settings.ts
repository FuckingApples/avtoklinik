import { useState, useEffect } from "react";
import { CarTableColumn, CarTableSettings } from "~/types/car";

export const DEFAULT_COLUMNS: CarTableColumn[] = [
  { key: "brand", title: "Марка", visible: true },
  { key: "model", title: "Модель", visible: true },
  { key: "year", title: "Год", visible: true },
  { key: "license_plate", title: "Гос. номер", visible: true },
  { key: "license_plate_region", title: "Страна регистрации", visible: true },
  { key: "client", title: "Владелец", visible: true },
  { key: "vin", title: "VIN", visible: true },
  { key: "mileage", title: "Пробег, км", visible: true },
  { key: "color", title: "Цвет", visible: true },
  { key: "actions", title: "Действия", visible: true }
];

const DEFAULT_SETTINGS: CarTableSettings = {
  columns: DEFAULT_COLUMNS,
  pageSize: 10
};

export function useCarTableSettings(orgId: string) {
  const storageKey = `car-table-settings-${orgId}`;
  const [settings, setSettings] = useState<CarTableSettings>(DEFAULT_SETTINGS);
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    try {
      const savedSettings = localStorage.getItem(storageKey);
      if (savedSettings) {
        const parsedSettings = JSON.parse(savedSettings) as CarTableSettings;

        const mergedColumns = DEFAULT_COLUMNS.map(defaultCol => {
          const savedCol = parsedSettings.columns.find(col => col.key === defaultCol.key);
          return savedCol || defaultCol;
        });
        
        setSettings({
          ...parsedSettings,
          columns: mergedColumns
        });
      }
    } catch (error) {
      console.error("Failed to load car table settings:", error);
    }
    
    setIsLoaded(true);
  }, [storageKey]);

  const saveSettings = (newSettings: CarTableSettings) => {
    try {
      localStorage.setItem(storageKey, JSON.stringify(newSettings));
      setSettings(newSettings);
    } catch (error) {
      console.error("Failed to save car table settings:", error);
    }
  };

  const resetSettings = () => {
    try {
      localStorage.removeItem(storageKey);
      setSettings(DEFAULT_SETTINGS);
    } catch (error) {
      console.error("Failed to reset car table settings:", error);
    }
  };

  return {
    settings,
    saveSettings,
    resetSettings,
    isLoaded,
    defaultSettings: DEFAULT_SETTINGS
  };
} 