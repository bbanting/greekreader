import { useState } from "react";
import { MantineProvider, AppShell, Header, Navbar } from '@mantine/core';
import { QueryClientProvider, QueryClient  } from "@tanstack/react-query";

import { AssetSelector } from './AssetSelector';
import { EditorWindow } from "./EditorWindow";


function App() {
  const [assetType, setAssetType] = useState<"books" | "helpsets">("books");
  const [assetID, setAssetID] = useState<number | null>(null);

  const queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryClient}>
    <MantineProvider withNormalizeCSS withGlobalStyles>
      <div className="App">
        <AppShell 
          padding={0} 
          navbar={
            <Navbar width={{base: 300}}>
              <AssetSelector setAssetID={setAssetID} setAssetType={setAssetType}/>
            </Navbar>}
          header={<Header height={50} p="xs">Header placeholder</Header>}
        >
          <EditorWindow assetID={assetID} assetType={assetType} />
        </AppShell>
      </div>
    </MantineProvider>
    </QueryClientProvider>
  );
}

export default App;
