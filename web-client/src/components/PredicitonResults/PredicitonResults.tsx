import { FC, useEffect, useRef, useState } from "react";
import "./PredicitonResults.scss";
import useModelContext from "@context/ModelContext";
import PredicitonResult from "./PredicitionResult";
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Typography,
} from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import useCanvasControlContext from "@context/CanvasControlContext";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";

export const PredicitonResults: FC = () => {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const [isEmpty, setIsEmpty] = useState<boolean>(false);
  const { prediction, session } = useModelContext();
  const { strokes } = useCanvasControlContext();
  const accordionRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (prediction?.length) {
      setIsOpen(true);
      setIsEmpty(false);

      accordionRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [prediction]);

  useEffect(() => {
    if (strokes === 0) {
      setIsOpen(false);
      // 300ms is MUI default collapse animation duration
      setTimeout(() => {
        setIsEmpty(true);
      }, 300);
      return;
    }
    setIsEmpty(true);
  }, [strokes, session]);

  const changeHandler = () => setIsOpen((prev) => !prev);

  return (
    <Accordion
      className="predictions-accordion"
      expanded={isOpen}
      disabled={!prediction?.length || (isEmpty && !strokes)}
      ref={accordionRef}
      onChange={changeHandler}
    >
      <AccordionSummary
        expandIcon={<ExpandMoreIcon sx={{ color: "#bfbfbf" }} />}
      >
        <Typography className="predictions-label">Predictions</Typography>
      </AccordionSummary>
      <AccordionDetails>
        <div className="predictions-container">
          {isEmpty ? (
            <div className="predictions-container--empty">
              <VisibilityOffIcon fontSize="large" />
              <span>
                Click <strong>Predict</strong> button <br />
                to see model's prediction
              </span>
            </div>
          ) : (
            prediction.map((p, index) => (
              <PredicitonResult key={index} prediction={p} />
            ))
          )}
        </div>
      </AccordionDetails>
    </Accordion>
  );
};

export default PredicitonResults;
