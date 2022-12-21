import { useState } from "react";
import { MantineProvider, AppShell, Header, Navbar, Text } from '@mantine/core';

import { AssetSelector } from './AssetSelector';
import { EditorWindow } from "./EditorWindow";


function App() {
  const [assetType, setAssetType] = useState<"book" | "helpset">("book");
  const [asset, setAsset] = useState<number | null>(null);

  return (
    <MantineProvider withNormalizeCSS withGlobalStyles>
      <div className="App">
        <AppShell 
          padding={0} 
          navbar={<Navbar width={{base: 300}}><AssetSelector/></Navbar>}
          header={<Header height={50} p="xs">Header placeholder</Header>}
        >
          <EditorWindow asset={asset} assetType={assetType} />
        </AppShell>
      </div>
    </MantineProvider>
  );
}

export default App;
