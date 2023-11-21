import { FC } from "react";
import { Button } from "@mui/material";
import useCanvasControlContext from "@context/CanvasControlContext";
import "./Controls.scss";

export const Controls: FC = () => {
  const { reset, undo, save } = useCanvasControlContext();

  return (
    <div className="controls">
      <Button size="large" onClick={reset}>
        Reset
      </Button>
      <Button size="large" onClick={undo}>
        Undo
      </Button>
      <Button size="large" onClick={save}>
        Save
      </Button>
    </div>
  );
};

export default Controls;
