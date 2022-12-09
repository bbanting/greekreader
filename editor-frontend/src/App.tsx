import { MantineProvider } from '@mantine/core';


function App() {
  return (
    <MantineProvider withNormalizeCSS withGlobalStyles>
      <div className="App">
        Editor app goes here.
      </div>
    </MantineProvider>
  );
}

export default App;
