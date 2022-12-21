import { useState, useEffect } from "react";
import { Accordion } from "@mantine/core";


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

interface HelpSet {
  id: number,
  settings: number | null,
  date_created: string,
  last_modified: string,
  name: string,
  creator: number
}


export function AssetSelector() {
  /**A component to select which asset to edit. */
    const [books, setBooks] = useState<Book[] | null>(null);
    const [helpSets, setHelpSets] = useState<HelpSet[] | null>(null);

    useEffect(() => {
      fetch("http://localhost:8000/api/edit/books/")
      .then(res => {console.log(res); return res.json();})
      .then(data => setBooks(data))
      .catch((error) => console.log(error));

      fetch("http://localhost:8000/api/edit/helpsets/")
      .then(res => {console.log(res); return res.json();})
      .then(data => setHelpSets(data))
      .catch((error) => console.log(error));
    }, [])

    return (
      <Accordion variant="filled" defaultValue={"books"}>
        <Accordion.Item value="books">
          <Accordion.Control>
            Books
          </Accordion.Control>
          <Accordion.Panel>
            <ul>
              {books?.map(b => <li>{b.name}</li>)}
            </ul>
          </Accordion.Panel>
        </Accordion.Item>
        <Accordion.Item value="helpsets">
          <Accordion.Control>
            Help Sets
          </Accordion.Control>
          <Accordion.Panel>
            <ul>
              {helpSets?.map(hs => <li>{hs.name}</li>)}
            </ul>
          </Accordion.Panel>
        </Accordion.Item>
      </Accordion>
    )
}
