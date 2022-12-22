import { useState, useEffect } from "react";
import { Accordion, Button } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { getBooks, getHelpsets } from "../api-tools";


interface AssetSelectorProps {
  setAssetID: (x: number) => void,
  setAssetType: (x: "book" | "helpset") => void
}


export function AssetSelector({setAssetID, setAssetType}: AssetSelectorProps) {
  /**A component to select which asset to edit. */
  const booksQuery = useQuery({queryKey: ["books"], queryFn: getBooks});
  const helpsetsQuery = useQuery({queryKey: ["helpsets"], queryFn: getHelpsets});

  return (
    <Accordion variant="filled" defaultValue={"books"}>
      <Accordion.Item value="books">
        <Accordion.Control>
          Books
        </Accordion.Control>
        <Accordion.Panel>
          {booksQuery.data?.map(b => 
            <Button key={b.id} fullWidth variant="subtle" onClick={() => {
              setAssetType("book");
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
              setAssetType("helpset");
              setAssetID(hs.id);
            }}>{hs.name}</Button>
          )}
        </Accordion.Panel>
      </Accordion.Item>
    </Accordion>
  );
}
