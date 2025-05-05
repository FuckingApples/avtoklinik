export interface HelpItem {
  title: string;
  description: string;
}

export interface HelpContent {
  title: string;
  items: HelpItem[];
  inheritDefault?: boolean;
}
