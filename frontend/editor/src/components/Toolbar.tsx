import { Text } from "@mantine/core";

import { Book, HelpSet } from "../api-types";


interface ToolbarProps {
  asset: Book | HelpSet | null
}

/**A generic toolbar component for any given editor. */
export function Toolbar(props: ToolbarProps) {
  return (
    <Text sx={{textAlign: "center"}}>Toolbar goes here</Text>
  )
}
