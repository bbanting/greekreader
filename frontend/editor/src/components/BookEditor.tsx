import { useState } from "react";
import { Text } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { Book } from "../api-types";
import { Toolbar } from "./Toolbar";
import { getSingleBook, getSingleChapter } from "../api-tools";


interface BookEditorProps {
  id: number
}


/**The editor component for book objects. */
export function BookEditor({ id }: BookEditorProps) {

  const [chapterId, setChapterId] = useState<number>(0);

  const bookQuery = useQuery({
    queryKey: ["book", id], 
    queryFn: () => getSingleBook(id),
    onSuccess: (data) => {if (!chapterId) setChapterId(data.chapters[0])}
  });

  const chapterQuery = useQuery({
    queryKey: ["chapter", chapterId],
    queryFn: () => getSingleChapter(chapterId),
    enabled: !!chapterId
  });

  return (
    <>
      <Toolbar>
        <Text sx={{textAlign: "center"}}>Toolbar item placeholder...</Text>
      </Toolbar>

      <Text>{bookQuery.data?.title}</Text>
      <Text>Chapter: {chapterQuery.data?.title}</Text>
    </>
  )
}
