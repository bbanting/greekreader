import { useState } from "react";
import { MantineProvider, AppShell, Header, Navbar, Text } from '@mantine/core';

import { AssetSelector } from './AssetSelector';
import { EditorWindow } from "./EditorWindow";


function App() {
  const [assetType, setAssetType] = useState<"books" | "helpsets">("books");
  const [assetID, setAssetID] = useState<number | null>(null);

  return (
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
  );
}

export default App;
