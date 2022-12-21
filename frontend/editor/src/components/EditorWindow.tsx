import { useEffect, useState } from "react";
import { Text, Container } from "@mantine/core";


interface EditorWindowProps {
  assetID: number | null, 
  assetType: "books" | "helpsets"
}


export function EditorWindow({assetID, assetType}: EditorWindowProps) {
  const [assetVal, setAssetVal] = useState<string | null>(null);

  useEffect(() => {
    if (assetID === null) return;
    fetch(`http://localhost:8000/api/edit/${assetType}/${assetID}/`)
      .then(res => res.json())
      .then(data => {
        assetType === "books" ? setAssetVal(data.title) : setAssetVal(data.name);
      })
      .catch((error) => console.log(error));
  }, [assetID])

  return (
    <Container>
      <Text sx={{textAlign: "center"}}>Toolbar goes here.</Text>
      {!assetID && <Text>Please select an asset to edit.</Text>}
      {assetID && <Text>{assetVal} is selected.</Text>}
    </Container>
  )
}