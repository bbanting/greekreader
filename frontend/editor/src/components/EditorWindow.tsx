import { useEffect, useState } from "react";
import { Text, Container } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { BookEditor } from "./BookEditor";
import { HelpsetEditor } from "./HelpsetEditor";


interface EditorWindowProps {
  assetID: number, 
  assetType: "books" | "helpsets"
}


export function EditorWindow({assetID, assetType}: EditorWindowProps) {
  let editor;
  if (assetID) {
    editor = (assetType === "books") 
      ? <BookEditor id={assetID} /> 
      : <HelpsetEditor id={assetID} />
  } else {
    editor = <Text>Please select an asset to edit.</Text>;
  }

  return (
    <Container>
      {editor}
    </Container>
  )
}
