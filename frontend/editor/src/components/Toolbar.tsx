import { ReactNode } from "react";


interface ToolbarProps {
  children: ReactNode
}

/**A generic toolbar component for any given editor. */
export function Toolbar(props: ToolbarProps) {
  return (
    <div>
      {props.children}
    </div>
  )
}
