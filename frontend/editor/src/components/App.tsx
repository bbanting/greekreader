import { useState } from "react";
import { MantineProvider, AppShell, Header, Navbar } from '@mantine/core';
import { QueryClientProvider, QueryClient  } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

import { AssetSelector } from './AssetSelector';
import { EditorWindow } from "./EditorWindow";


function App() {
  const [assetType, setAssetType] = useState<"book" | "helpset">("book");
  const [assetID, setAssetID] = useState<number>(0);

  const queryClient = new QueryClient();

  const appShell = 
  <AppShell 
    padding={0} 
    navbar={
      <Navbar width={{base: 300}}>
        <AssetSelector setAssetID={setAssetID} setAssetType={setAssetType}/>
      </Navbar>
    }
    header={<Header height={50} p="xs">Header placeholder</Header>}
  >
    <EditorWindow assetID={assetID} assetType={assetType} />
  </AppShell>

  return (
    <QueryClientProvider client={queryClient}>
    <ReactQueryDevtools initialIsOpen={false} />
    <MantineProvider withNormalizeCSS withGlobalStyles>
      <div className="App">
        {appShell}
      </div>
    </MantineProvider>
    </QueryClientProvider>
  );
}

export default App;
