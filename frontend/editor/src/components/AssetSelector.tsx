import { useState, useEffect } from "react";
import { Accordion, Button } from "@mantine/core";

import { Book, HelpSet } from "../api-types";


interface AssetSelectorProps {
  setAssetID: (x: number | null) => void,
  setAssetType: (x: "books" | "helpsets") => void
}


export function AssetSelector({setAssetID, setAssetType}: AssetSelectorProps) {
  /**A component to select which asset to edit. */
    const [books, setBooks] = useState<Book[] | null>(null);
    const [helpSets, setHelpSets] = useState<HelpSet[] | null>(null);

    useEffect(() => {
      fetch("http://localhost:8000/api/edit/books/")
      .then(res => res.json())
      .then(data => setBooks(data))
      .catch((error) => console.log(error));

      fetch("http://localhost:8000/api/edit/helpsets/")
      .then(res => res.json())
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
            {books?.map(b => 
              <Button key={b.id} fullWidth variant="subtle" onClick={() => {
                setAssetType("books");
                setAssetID(b.id);
              }}>{b.title}</Button>
            )}
          </Accordion.Panel>
        </Accordion.Item>
        <Accordion.Item value="helpsets">
          <Accordion.Control>
            Help Sets
          </Accordion.Control>
          <Accordion.Panel>
            {helpSets?.map(hs => 
              <Button key={hs.id} fullWidth variant="subtle" onClick={() => {
                setAssetType("helpsets");
                setAssetID(hs.id);
              }}>{hs.name}</Button>
            )}
          </Accordion.Panel>
        </Accordion.Item>
      </Accordion>
    )
}
