import { useState } from "react";
import { Text, Select } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { Book } from "../api-types";
import { Toolbar } from "./Toolbar";
import { getSingleBook, getSingleChapter } from "../api-tools";


interface BookEditorProps {
  bookId: number
}


/**The editor component for book objects. */
export function BookEditor({ bookId }: BookEditorProps) {

  const [chapterId, setChapterId] = useState<number>(0);

  const bookQuery = useQuery({
    queryKey: ["book", bookId], 
    queryFn: () => getSingleBook(bookId),
    onSuccess: (data) => setChapterId(data.chapters[0].id)
  });

  const chapterQuery = useQuery({
    queryKey: ["chapter", bookId, chapterId],
    queryFn: () => getSingleChapter(chapterId),
    enabled: !!chapterId
  });


  return (
    <>
      <Toolbar>
        <Text sx={{textAlign: "center"}}>Toolbar item placeholder...</Text>
      </Toolbar>

      <Text>{bookQuery.data?.title}</Text>
      <Text>{chapterQuery.data?.title}</Text>
      <Text>{chapterQuery.data?.content}</Text>
    </>
  )
}


interface ChapterSelectProps {
  setChapterId: () => void
}

function ChapterSelect() {

}