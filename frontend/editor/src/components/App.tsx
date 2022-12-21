import { MantineProvider, AppShell, Header, Navbar, Text } from '@mantine/core';

import { AssetSelector } from './AssetSelector';


function App() {
  return (
    <MantineProvider withNormalizeCSS withGlobalStyles>
      <div className="App">
        <AppShell 
          padding={0} 
          navbar={<Navbar width={{base: 300}}><AssetSelector/></Navbar>}
          header={<Header height={50} p="xs">Header placeholder</Header>}
        >
          <Text sx={{textAlign: "center"}}>Toolbar goes here.</Text>
        </AppShell>
      </div>
    </MantineProvider>
  );
}

export default App;
