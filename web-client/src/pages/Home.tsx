import { Page } from "@components/Page";
import { Wrapper } from "@components/Wrapper";
import { Button, ButtonGroup } from "@mui/material";
import { FC, useState } from "react";

export const Home: FC = () => {
  const [selected, setSelected] = useState<number>(0);

  return (
    <Page center>
      <ButtonGroup
        variant="text"
        aria-label="text button group"
        color="primary"
        onChange={(e) => console.log(e)}
      >
        <Button
          color={selected == 0 ? "secondary" : "primary"}
          onClick={() => setSelected(0)}
        >
          Hiragana
        </Button>
        <Button
          color={selected == 1 ? "secondary" : "primary"}
          onClick={() => setSelected(1)}
        >
          Katakana
        </Button>
        <Button
          color={selected == 2 ? "secondary" : "primary"}
          onClick={() => setSelected(2)}
        >
          Kanji
        </Button>
      </ButtonGroup>
      <Wrapper />
    </Page>
  );
};
