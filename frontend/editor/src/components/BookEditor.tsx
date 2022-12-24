import { useState } from "react";
import { Text, Select } from "@mantine/core";
import { useQuery } from "@tanstack/react-query";

import { Chapter } from "../api-types";
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
        {bookQuery.isSuccess && chapterQuery.isSuccess && 
          <ChapterSelect 
            chapters={bookQuery.data?.chapters} 
            currentChapter={chapterQuery.data} 
            setChapterId={setChapterId} />}
        
      </Toolbar>

      <Text>{bookQuery.data?.title}</Text>
      <Text>{chapterQuery.data?.title}</Text>
      <Text>{chapterQuery.data?.content}</Text>
    </>
  )
}


interface ChapterSelectProps {
  chapters: Chapter[],
  currentChapter: Chapter,
  setChapterId: (x: number) => void
}

function ChapterSelect({chapters, currentChapter, setChapterId}: ChapterSelectProps) {
  const data = chapters.map((c) => ({value: c.id.toString(), label: `${c.ordinal_text}: ${c.title}`}))

  return (
    <Select 
      data={data}
      onChange = {(v) => setChapterId(Number(v))}
      dropdownPosition = {"bottom"}
      value = {currentChapter.id.toString()}
    />
  )
}
