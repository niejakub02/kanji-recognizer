import { Canvas } from "@components/Canvas";
import { Controls } from "@components/Controls";
import useCanvasControlContext from "@context/CanvasControlContext";
import { FC } from "react";
import "./Wrapper.scss";

export const Wrapper: FC = () => {
  const { ref, setStrokes } = useCanvasControlContext();

  const handleStrokeAdd = () => setStrokes((prev) => prev + 1);

  return (
    <div className="wrapper">
      <Canvas ref={ref} onStrokeAdd={handleStrokeAdd} />
      <Controls />
    </div>
  );
};

export default Wrapper;
