import { Text } from "@mantine/core";

import { HelpSet } from "../api-types";


interface HelpsetEditorProps {
  helpset: HelpSet
}


export function BookEditor({ helpset }:HelpsetEditorProps) {
  return (
    <Text>{helpset.name}</Text>
  )
}
