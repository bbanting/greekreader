import { useEffect, useState } from "react";
import { Text, Container } from "@mantine/core";


interface EditorWindowProps {
  asset: number | null, 
  assetType: "books" | "helpsets"
}


export function EditorWindow({asset, assetType}: EditorWindowProps) {
  const [assetVal, setAssetVal] = useState<string | null>(null);

  useEffect(() => {
    if (asset === null) return;
    fetch(`http://localhost:8000/api/edit/${assetType}/${asset}/`)
      .then(res => res.json())
      .then(data => {
        assetType === "books" ? setAssetVal(data.title) : setAssetVal(data.name);
      })
      .catch((error) => console.log(error));
  }, [asset])

  return (
    <Container>
      <Text sx={{textAlign: "center"}}>Toolbar goes here.</Text>
      {!asset && <Text>Please select an asset to edit.</Text>}
      {asset && <Text>{assetVal} is selected.</Text>}
    </Container>
  )
}