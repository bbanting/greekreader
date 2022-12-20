import { useState, useEffect } from "react";


interface Book {
  id: number,
  chapters: number[],
  date_created: string,
  last_modified: string,
  name: string,
  tier: number,
  creator: number,
  cover_image: number | null,
  helpset: number | null,
  fallback_helpset: number | null
}

export function AssetSelector() {
  /**A component to select which asset to edit. */
    const [books, setBooks] = useState<Book[] | null>(null);

    useEffect(() => {
      fetch("http://localhost:8000/api/edit/books/")
      .then(res => res.json())
      .then(data => setBooks(data));
    }, [])

    return (
      <ul>
        {books?.map(b => (<li key={b.id}>{b.name}</li>))}
      </ul>
    )
}