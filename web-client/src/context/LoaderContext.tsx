import { Backdrop, CircularProgress } from "@mui/material";
import { FC, ReactNode, createContext, useContext, useState } from "react";

type LoaderContext = {
  isLoading: boolean;
  setIsLoading: (value: boolean) => void;
};

type LoaderProviderProps = {
  children: ReactNode;
};

const context = createContext<LoaderContext>({} as LoaderContext);

export const LoaderProvider: FC<LoaderProviderProps> = ({ children }) => {
  const [isLoading, setIsLoading] = useState<boolean>(true);

  return (
    <context.Provider value={{ isLoading, setIsLoading }}>
      <Backdrop
        sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}
        open={isLoading}
      >
        <CircularProgress size={50} thickness={6} />
      </Backdrop>
      {children}
    </context.Provider>
  );
};

export const useLoaderContext = () => useContext(context);

export default useLoaderContext;
