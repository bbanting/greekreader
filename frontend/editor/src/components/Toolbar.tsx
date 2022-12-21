import { Text } from "@mantine/core";

import { Book, HelpSet } from "./AssetSelector";


interface ToolbarProps {
  asset: Book | HelpSet | null
}


export function Toolbar(props: ToolbarProps) {
  return (
    <Text sx={{textAlign: "center"}}>Toolbar goes here</Text>
  )
}
