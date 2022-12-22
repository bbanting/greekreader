import { Text } from "@mantine/core";

import { Book } from "../api-types";


interface BookEditorProps {
  book: Book
}


export function BookEditor({ book }: BookEditorProps) {
  return (
    <Text>{book.title}</Text>
  )
}
