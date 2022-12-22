import { Text } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { Book } from "../api-types";
import { Toolbar } from "./Toolbar";
import { getSingleBook, getSingleHelpset } from "../api-tools";


interface BookEditorProps {
  id: number
}


/**The editor component for book objects. */
export function BookEditor({ id }: BookEditorProps) {
  const bookQuery = useQuery({
    queryKey: ["book", id], 
    queryFn: () => getSingleBook(id)
  });

  return (
    <>
      <Toolbar>
        <Text sx={{textAlign: "center"}}>Toolbar item placeholder...</Text>
      </Toolbar>

      <Text>{bookQuery.data?.title}</Text>
    </>
  )
}
