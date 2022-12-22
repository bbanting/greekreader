import { useState, useEffect } from "react";
import { Accordion, Button } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { Book, HelpSet } from "../api-types";


interface AssetSelectorProps {
  setAssetID: (x: number | null) => void,
  setAssetType: (x: "books" | "helpsets") => void
}


async function getBooks(): Promise<Book[]> {
  const res = await fetch("http://localhost:8000/api/edit/books/");
  return await res.json();
}

async function getHelpsets(): Promise<HelpSet[]> {
  const res = await fetch("http://localhost:8000/api/edit/helpsets/");
  return await res.json();
}


export function AssetSelector({setAssetID, setAssetType}: AssetSelectorProps) {
  /**A component to select which asset to edit. */

  const booksQuery = useQuery({queryKey: ["books"], queryFn: getBooks})
  const helpsetsQuery = useQuery({queryKey: ["helpsets"], queryFn: getHelpsets})

  return (
    <Accordion variant="filled" defaultValue={"books"}>
      <Accordion.Item value="books">
        <Accordion.Control>
          Books
        </Accordion.Control>
        <Accordion.Panel>
          {booksQuery.data?.map(b => 
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
          {helpsetsQuery.data?.map(hs => 
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
