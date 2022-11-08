import React from 'react';
import './App.css';
import { Box, CssBaseline, ThemeProvider } from "@mui/material";
import { createTheme } from "@mui/material/styles";
import { routes as appRoutes } from "./routes";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

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
  
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box height="100vh" display="flex" flexDirection="column" >
        <Router>
          <Routes>
            {
              appRoutes.map(route => (
                <Route 
                  key={route.key}
                  path={route.path}
                  element={<route.component />}
                />
              ))
            }
          </Routes>
        </Router>
      </Box>
    </ThemeProvider>
  );
}

export default App;
