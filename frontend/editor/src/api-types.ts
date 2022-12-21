export interface Book {
  id: number,
  chapters: number[],
  date_created: string,
  last_modified: string,
  title: string,
  tier: number,
  creator: number,
  cover_image: number | null,
  helpset: number | null,
  fallback_helpset: number | null
}
  
export interface HelpSet {
  id: number,
  settings: number | null,
  date_created: string,
  last_modified: string,
  name: string,
  creator: number
}
  