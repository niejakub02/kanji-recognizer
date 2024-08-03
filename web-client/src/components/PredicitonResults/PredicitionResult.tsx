import { FC, MouseEvent, useState } from "react";
import "./PredicitonResults.scss";
import { Prediction } from "@interfaces/common";
import { Tooltip } from "@mui/material";

interface PredicitonResultProps {
  prediction: Prediction;
}
export const PredicitonResult: FC<PredicitonResultProps> = ({ prediction }) => {
  const [tooltipVisibility, setTooltipVisibility] = useState(false);

  const clickHandler = (e: MouseEvent, literal: string) => {
    if (e.ctrlKey) {
      const link = document.createElement("a");
      link.setAttribute("href", `https://jisho.org/search/${literal}`);
      link.setAttribute("target", "_blank");
      link.click();
    } else {
      navigator.clipboard.writeText(literal);
      setTooltipVisibility(true);
    }
  };

  return (
    <div className="prediction">
      <Tooltip
        title="Copied to clipboard!"
        placement="bottom"
        open={tooltipVisibility}
      >
        <div
          className="prediction__literal"
          onClick={(e) => clickHandler(e, prediction.literal)}
          onMouseLeave={() => setTooltipVisibility(false)}
        >
          {prediction.literal}
        </div>
      </Tooltip>
      <div className="prediction__value">
        {(prediction.value * 100).toFixed(2)}%
      </div>
    </div>
  );
};

export default PredicitonResult;
