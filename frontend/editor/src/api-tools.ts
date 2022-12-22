import { Book, HelpSet } from "./api-types";


export async function getBooks(): Promise<Book[]> {
  /**Get all books from the api. */
  const res = await fetch("http://localhost:8000/api/edit/books/");
  return await res.json();
}

export async function getSingleBook(id:number): Promise<Book> {
  /**Get a single book from the api. */
  const res = await fetch(`http://localhost:8000/api/edit/books/${id}/`);
  return await res.json();
}
  
export async function getHelpsets(): Promise<HelpSet[]> {
  /**Get all help sets from the api. */
  const res = await fetch("http://localhost:8000/api/edit/helpsets/");
  return await res.json();
}

export async function getSingleHelpset(id:number): Promise<HelpSet> {
  /**Get a single help set from the api. */
  const res = await fetch(`http://localhost:8000/api/edit/helpsets/${id}/`);
  return await res.json();
}
