import { Canvas } from "@components/Canvas";
import { Controls } from "@components/Controls";
import useCanvasControlContext from "@context/CanvasControlContext";
import { FC } from "react";
import "./Wrapper.scss";

export const Wrapper: FC = () => {
  const { ref } = useCanvasControlContext();

  return (
    <div className="wrapper">
      <Canvas ref={ref} />
      <Controls />
    </div>
  );
};

export default Wrapper;
