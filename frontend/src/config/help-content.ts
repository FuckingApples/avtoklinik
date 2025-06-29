import type { HelpContent } from "~/types/help-menu";

export const helpContent: Record<string, HelpContent> = {
  default: {
    title: "Помощь",
    items: [
      {
        title: "Поддержка",
        description:
          "Если у вас возникли вопросы, напишите нам на example@example.com",
      },
      {
        title: "Открыть документацию",
        description: "Перейти на страницу документации",
        url: "https://docs.example.com",
      },
    ],
  },
  cars: {
    title: "Помощь по автомобилям",
    items: [
      {
        title: "Добавление автомобиля",
        description:
          'Нажмите "Добавить", чтобы создать новую запись автомобиля.',
      },
    ],
    inheritDefault: true,
  },
  registries: {
    title: "Помощь по справочникам",
    items: [
      {
        title: "Работа со справочником",
        description:
          "Справочник содержит необходимые для работы данные, которые можно редактировать.",
      },
      {
        title: "Добавление записей",
        description:
          'Выберите нужный раздел и нажмите "Добавить" для создания новой записи.',
      },
    ],
    inheritDefault: true,
  },
};

export function getHelpContent(
  pageKey: keyof typeof helpContent = "default",
): HelpContent {
  const defaultContent = helpContent.default ?? {
    title: "Помощь",
    items: [],
  };

  const pageContent = helpContent[pageKey];
  if (!pageContent) {
    return defaultContent;
  }

  if (pageContent.inheritDefault) {
    return {
      title: pageContent.title,
      items: [...pageContent.items, ...defaultContent.items],
    };
  }

  return pageContent;
}
