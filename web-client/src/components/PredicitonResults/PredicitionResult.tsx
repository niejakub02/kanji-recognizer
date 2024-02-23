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
      <div className="prediction__value">{(prediction.value * 100).toFixed(2)}%</div>
    </div>
  );
};

export default PredicitonResult;
