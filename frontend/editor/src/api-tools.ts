import { Book, Chapter, HelpSet } from "./api-types";

const BASE_URL = "http://localhost:8000/api/edit/";

/**Get all books from the api. */
export async function getBooks(): Promise<Book[]> {
  const res = await fetch(BASE_URL + "books/");
  return await res.json();
}

/**Get a single book from the api. */
export async function getSingleBook(id:number): Promise<Book> {
  const res = await fetch(BASE_URL + `books/${id}/`);
  return await res.json();
}
  
/**Get all help sets from the api. */
export async function getHelpsets(): Promise<HelpSet[]> {
  const res = await fetch(BASE_URL + "helpsets/");
  return await res.json();
}

/**Get a single help set from the api. */
export async function getSingleHelpset(id:number): Promise<HelpSet> {
  const res = await fetch(BASE_URL + `helpsets/${id}/`);
  return await res.json();
}

/**Get a single chapter from the api. */
export async function getSingleChapter(id: number): Promise<Chapter> {
  const res = await fetch(BASE_URL + `chapters/${id}/`);
  return await res.json();
}
