import { Text } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { HelpSet } from "../api-types";
import { getSingleBook, getSingleHelpset } from "../api-tools";


interface HelpsetEditorProps {
  id: number
}


export function HelpsetEditor({ id }:HelpsetEditorProps) {
  const helpsetQuery = useQuery({
    queryKey: ["helpset", id], 
    queryFn: () => getSingleHelpset(id)
  });

  return (
    <Text>{helpsetQuery?.data?.name}</Text>
  )
}
