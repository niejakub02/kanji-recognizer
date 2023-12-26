import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Home } from "@pages/Home";
import { createTheme, ThemeProvider } from "@mui/material";
import { CanvasControlProvider } from "@context/CanvasControlContext";
import { ModelProvider } from "@context/ModelContext";
import { LoaderProvider } from "@context/LoaderContext";

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
    text: {
      primary: "#bfbfbf",
    },
    primary: {
      main: "#ff4b41",
    },
    secondary: {
      main: "#a61300",
    },
    background: {
      default: "#ffffff",
      paper: "#242424",
    },
    divider: "#363535",
  },
});

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <LoaderProvider>
        <ModelProvider>
          <CanvasControlProvider>
            <RouterProvider router={router} />
          </CanvasControlProvider>
        </ModelProvider>
      </LoaderProvider>
    </ThemeProvider>
  </React.StrictMode>
);
