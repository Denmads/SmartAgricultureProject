import React from 'react';
import './App.css';
import { Box, CssBaseline } from "@mui/material";
import { createTheme, Experimental_CssVarsProvider as CssVarsProvider, experimental_extendTheme as extendTheme } from "@mui/material/styles";
import { routes as appRoutes } from "./routes";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from './components/NavigationBar';
import { QueryClient, QueryClientProvider } from "react-query";

function App() {
  const theme = createTheme({
    palette: {
      primary: {
        main: '#93aa5e',
      },
      secondary: {
        main: '#66c5ad',
      }
    }
  });

  const cssTheme = extendTheme(theme);

  const queryClient = new QueryClient();
  
  return (
      <QueryClientProvider client={queryClient}>
        <CssVarsProvider theme={cssTheme}>
          <CssBaseline />
          <Box height="100vh" display="flex" flexDirection="column" >
            
            <Router>
              <Routes>
                {
                  appRoutes.map(route => (
                    <Route 
                      key={route.key}
                      path={route.path}
                      element={<><NavBar /><route.component /></>}
                    />
                  ))
                }
              </Routes>
            </Router>
          </Box>
        </CssVarsProvider>
      </QueryClientProvider>
  );
}

export default App;
