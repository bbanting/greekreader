import { MantineProvider } from '@mantine/core';


function App() {
  return (
    <MantineProvider withNormalizeCSS withGlobalStyles>
      <div className="App">
        Reader app goes here.
      </div>
    </MantineProvider>
  );
}

export default App;
