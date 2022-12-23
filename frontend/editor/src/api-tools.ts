import { Book, Chapter, HelpSet } from "./api-types";


/**Get all books from the api. */
export async function getBooks(): Promise<Book[]> {
  const res = await fetch("http://localhost:8000/api/edit/books/");
  return await res.json();
}

/**Get a single book from the api. */
export async function getSingleBook(id:number): Promise<Book> {
  const res = await fetch(`http://localhost:8000/api/edit/books/${id}/`);
  return await res.json();
}
  
/**Get all help sets from the api. */
export async function getHelpsets(): Promise<HelpSet[]> {
  const res = await fetch("http://localhost:8000/api/edit/helpsets/");
  return await res.json();
}

/**Get a single help set from the api. */
export async function getSingleHelpset(id:number): Promise<HelpSet> {
  const res = await fetch(`http://localhost:8000/api/edit/helpsets/${id}/`);
  return await res.json();
}

/**Get a single chapter from the api. */
export async function getSingleChapter(id: number): Promise<Chapter> {
  const res = await fetch(`http://localhost:8000/api/edit/chapters/${id}/`);
  return await res.json();
}
