import { Page } from "@components/Page";
import { PredicitonResults } from "@components/PredicitonResults";
import { Wrapper } from "@components/Wrapper";
import { FC } from "react";

export const Home: FC = () => {
  return (
    <Page center>
      <PredicitonResults />
      <Wrapper />
    </Page>
  );
};
