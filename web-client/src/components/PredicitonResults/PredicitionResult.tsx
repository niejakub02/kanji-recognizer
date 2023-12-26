import { FC } from "react";
import "./PredicitonResults.scss";
import { Prediction } from "@interfaces/common";

interface PredicitonResultProps {
  prediction: Prediction;
}
export const PredicitonResult: FC<PredicitonResultProps> = ({ prediction }) => {
  return (
    <div className="prediction">
      <div className="prediction__literal">{prediction.literal}</div>
      <div className="prediction__value">{prediction.value.toFixed(4)}</div>
    </div>
  );
};

export default PredicitonResult;
