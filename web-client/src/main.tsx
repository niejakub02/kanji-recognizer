import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Home } from "@pages/Home";
import { createTheme, ThemeProvider } from "@mui/material";
import { CanvasControlProvider } from "@context/CanvasControlContext";
import { ModelProvider } from "@context/ModelContext";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/suavemente",
    element: <p>essa</p>,
  },
]);

const theme = createTheme({
  palette: {
    primary: {
      main: "#ff4b41",
    },
    secondary: {
      main: "#a61300",
    },
  },
});

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <ModelProvider>
        <CanvasControlProvider>
          <RouterProvider router={router} />
        </CanvasControlProvider>
      </ModelProvider>
    </ThemeProvider>
  </React.StrictMode>
);
