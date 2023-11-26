import { Tensor } from "onnxruntime-web";
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

// export const www = () => {
//   const img = new Image(64, 64);
//   img.src = "./../test_image.png";
//   img.addEventListener("load", async () => {
//     const virtualCanvas = document.createElement("canvas");
//     virtualCanvas.height = 64;
//     virtualCanvas.width = 64;
//     const virtualCtx = virtualCanvas.getContext("2d")!;
//     // virtualCtx.fillStyle = "black";
//     virtualCtx.fillRect(0, 0, virtualCanvas.width, virtualCanvas.height);
//     virtualCtx.drawImage(img, 0, 0, 64, 64);
//     const uintarray = virtualCtx.getImageData(0, 0, 64, 64);
//     const accarr = [];
//     for (let i = 0; i < uintarray.data.length; i += 4) {
//       accarr.push(
//         (0.299 * uintarray.data[i] +
//           0.587 * uintarray.data[i + 1] +
//           0.114 * uintarray.data[i + 2]) /
//           255.0
//       );
//     }
//     const float32Data = Float32Array.from(accarr);
//     const inputTensor = new Tensor("float32", float32Data, [1, 1, 64, 64]);
// }

export const convertCanvasToTensor = (canvas: HTMLCanvasElement) => {
  const context = canvas.getContext("2d");

  if (!context) return;
  const uintarray = context.getImageData(0, 0, 64, 64);
  const grayscaleArray = [];

  for (let i = 0; i < uintarray.data.length; i += 4) {
    grayscaleArray.push(
      (0.299 * uintarray.data[i] +
        0.587 * uintarray.data[i + 1] +
        0.114 * uintarray.data[i + 2]) /
        255.0
    );
  }
  const float32Data = Float32Array.from(grayscaleArray);
  // TODO: resize image to 64x64
  return new Tensor("float32", float32Data, [1, 1, 64, 64]);
};
