import { Book, HelpSet } from "./api-types";


export async function getBooks(): Promise<Book[]> {
  /**Get all books from the api. */
  const res = await fetch("http://localhost:8000/api/edit/books/");
  return await res.json();
}
  
export async function getHelpsets(): Promise<HelpSet[]> {
  /**Get all helpsets from the api. */
  const res = await fetch("http://localhost:8000/api/edit/helpsets/");
  return await res.json();
}