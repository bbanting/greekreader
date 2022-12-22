import { useEffect, useState } from "react";
import { Text, Container } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { Toolbar } from "./Toolbar";
import { HelpSet, Book } from "../api-types";
import { getSingleBook, getSingleHelpset } from "../api-tools";


interface EditorWindowProps {
  assetID: number, 
  assetType: "books" | "helpsets"
}


export function EditorWindow({assetID, assetType}: EditorWindowProps) {
  const bookQuery = useQuery({
    queryKey: ["book"], 
    queryFn: () => getSingleBook(assetID), 
    enabled: assetType === "books" && assetID > 0
  });

  const helpsetQuery = useQuery({
    queryKey: ["helpset"], 
    queryFn: () => getSingleHelpset(assetID), 
    enabled: assetType === "helpsets" && assetID > 0
  });

  return (
    <Container>
      <Toolbar asset={bookQuery.data || helpsetQuery.data || null} />
      {!assetID && <Text>Please select an asset to edit.</Text>}
      {assetType === "books" && bookQuery.data && <Text>{bookQuery.data.title}</Text>}
      {assetType === "helpsets" && helpsetQuery.data && <Text>{helpsetQuery.data.name}</Text>}
    </Container>
  )
}
