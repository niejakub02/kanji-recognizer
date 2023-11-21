import { Page } from "@components/Page";
import { Wrapper } from "@components/Wrapper";
import { CanvasControlProvider } from "@context/CanvasControlContext";
import { FC } from "react";

export const Home: FC = () => {
  return (
    <CanvasControlProvider>
      <Page center>
        <Wrapper />
      </Page>
    </CanvasControlProvider>
  );
};
