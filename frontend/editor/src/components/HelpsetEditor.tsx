import { Text } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { HelpSet } from "../api-types";
import { Toolbar } from "./Toolbar";
import { getSingleBook, getSingleHelpset } from "../api-tools";


interface HelpsetEditorProps {
  id: number
}


/**The editor component for help set objects. */
export function HelpsetEditor({ id }:HelpsetEditorProps) {
  const helpsetQuery = useQuery({
    queryKey: ["helpset", id], 
    queryFn: () => getSingleHelpset(id)
  });

  return (
    <>
      <Toolbar>
        <Text sx={{textAlign: "center"}}>Toolbar item placeholder...</Text>
      </Toolbar>

      <Text>{helpsetQuery?.data?.name}</Text>
    </>
  )
}
