import { useEffect, useState } from "react";
import { Text, Container } from "@mantine/core";

import { Toolbar } from "./Toolbar";
import { HelpSet, Book } from "../api-types";


interface EditorWindowProps {
  assetID: number | null, 
  assetType: "books" | "helpsets"
}


export function EditorWindow({assetID, assetType}: EditorWindowProps) {
  const [assetVal, setAssetVal] = useState<Book & HelpSet | null>(null);

  useEffect(() => {
    if (assetID === null) return;
    fetch(`http://localhost:8000/api/edit/${assetType}/${assetID}/`)
      .then(res => res.json())
      .then(data => {
        setAssetVal(data);
      })
      .catch((error) => console.log(error));
  }, [assetID])

  return (
    <Container>
      <Toolbar asset={assetVal} />
      {!assetID && <Text>Please select an asset to edit.</Text>}
      {assetID && <Text>{assetVal && (assetVal.title ? assetVal.title : assetVal.name)}</Text>}
    </Container>
  )
}