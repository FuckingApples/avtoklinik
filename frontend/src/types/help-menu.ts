export interface HelpItem {
  title: string;
  description: string;
  url?: string;
}

export interface HelpContent {
  title: string;
  items: HelpItem[];
  inheritDefault?: boolean;
}
