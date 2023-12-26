import { ChangeEvent, FC, useRef } from "react";
import { Button } from "@mui/material";
import useCanvasControlContext from "@context/CanvasControlContext";
import "./Controls.scss";
import useModelContext from "@context/ModelContext";
import { convertCanvasToTensor } from "@utils/canvasUtils";
import useLoaderContext from "@context/LoaderContext";
import { ModelsMenu } from "@components/ModelsMenu";

export const Controls: FC = () => {
  const { strokes, reset, undo, save, load, getCompoundImage } =
    useCanvasControlContext();
  const { predict } = useModelContext();
  const { setIsLoading } = useLoaderContext();
  const fileInput = useRef<HTMLInputElement>(null);

  const predictFromImage = async () => {
    setIsLoading(true);
    setTimeout(async () => {
      const canvas = getCompoundImage(true, true);

      if (!canvas) return;
      const tensor = convertCanvasToTensor(canvas);

      if (!tensor) return;
      await predict(tensor);
      setIsLoading(false);
    }, 0);
  };

  const triggerFileLoad = () => fileInput.current?.click();

  const handleLoad = (e: ChangeEvent<HTMLInputElement>) => {
    load(e);
    if (fileInput.current?.value) fileInput.current.value = "";
  };

  return (
    <div className="controls">
      <ModelsMenu />
      <Button size="large" onClick={undo}>
        Undo
      </Button>
      <Button size="large" onClick={save}>
        Save
      </Button>
      <Button
        onClick={predictFromImage}
        size="large"
        variant="outlined"
        className="control row--2"
        disabled={!strokes}
      >
        Predict
      </Button>
      <Button size="large" onClick={reset}>
        Reset
      </Button>
      <input
        ref={fileInput}
        className="control--hidden"
        type="file"
        onInput={handleLoad}
      />
      <Button size="large" onClick={triggerFileLoad}>
        Load
      </Button>
    </div>
  );
};

export default Controls;
