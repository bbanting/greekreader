import { Text, Container } from "@mantine/core";


interface EditorWindowProps {
  asset: number | null, 
  assetType: "book" | "helpset"
}

export function EditorWindow({asset, assetType}: EditorWindowProps) {
  return (
    <Container>
      <Text sx={{textAlign: "center"}}>Toolbar goes here.</Text>
      {!asset && <Text>Please select an asset to edit.</Text>}
    </Container>
  )
}