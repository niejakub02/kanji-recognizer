import { CANVAS_HEIGHT, CANVAS_WIDTH } from "./constants";

export const createCanvas = () => {
  const newCanvas = document.createElement("canvas");
  newCanvas.classList.add("canvas");
  newCanvas.height = CANVAS_HEIGHT;
  newCanvas.width = CANVAS_WIDTH;
  //   const uuid = crypto.randomUUID();
  //   newCanvas.setAttribute("uuid", uuid);
  return newCanvas;
};

export const drawSolidLine = (
  context: CanvasRenderingContext2D,
  x: number,
  y: number
) => {
  context.lineWidth = 16;
  context.lineCap = "round";
  context.lineJoin = "round";
  context.strokeStyle = "white";
  context.lineTo(x, y);
  context.stroke();
  context.beginPath();
  context.moveTo(x, y);
};
