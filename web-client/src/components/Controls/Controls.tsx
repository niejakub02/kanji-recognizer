import { FC } from "react";
import { Button } from "@mui/material";
import useCanvasControlContext from "@context/CanvasControlContext";
import "./Controls.scss";
import useModelContext from "@context/ModelContext";
import { convertCanvasToTensor } from "@utils/canvasUtils";

export const Controls: FC = () => {
  const { reset, undo, save, getCompoundImage } = useCanvasControlContext();
  const { predict } = useModelContext();

  const predictFromImage = () => {
    const canvas = getCompoundImage();

    if (!canvas) return;
    const tensor = convertCanvasToTensor(canvas);

    if (!tensor) return;
    predict(tensor);
  };

  return (
    <div className="controls">
      <Button size="large" onClick={reset}>
        Reset
      </Button>
      <Button size="large" onClick={undo}>
        Undo
      </Button>
      <Button color="secondary" size="large" onClick={predictFromImage}>
        Predict
      </Button>
      <Button color="secondary" size="large" onClick={save}>
        Save
      </Button>
    </div>
  );
};

export default Controls;
