import { useEffect, useRef, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { InferenceSession, Tensor } from "onnxruntime-web";

function App() {
  const [count, setCount] = useState(0);
  const reff = useRef<HTMLDivElement>(null);

  useEffect(() => {
    (async () => {
      const img = new Image(64, 64);
      img.src = "./../test_image.png";
      img.addEventListener("load", async () => {
        const virtualCanvas = document.createElement("canvas");
        virtualCanvas.height = 64;
        virtualCanvas.width = 64;
        const virtualCtx = virtualCanvas.getContext("2d")!;
        // virtualCtx.fillStyle = "black";
        virtualCtx.fillRect(0, 0, virtualCanvas.width, virtualCanvas.height);
        virtualCtx.drawImage(img, 0, 0, 64, 64);
        const uintarray = virtualCtx.getImageData(0, 0, 64, 64);
        const accarr = [];
        for (let i = 0; i < uintarray.data.length; i += 4) {
          accarr.push(
            (0.299 * uintarray.data[i] +
              0.587 * uintarray.data[i + 1] +
              0.114 * uintarray.data[i + 2]) /
              255.0
          );
        }
        const float32Data = Float32Array.from(accarr);
        const inputTensor = new Tensor("float32", float32Data, [1, 1, 64, 64]);

        const session = await InferenceSession.create("./../best_go.onnx");
        const feeds: Record<string, Tensor> = {};
        feeds[session.inputNames[0]] = inputTensor;
        const outputData = await session.run(feeds);
        const output: Tensor & { cpuData: number[] } = outputData[
          session.outputNames[0]
        ] as Tensor & { cpuData: number[] };
        console.log(output.cpuData.indexOf(Math.max(...output.cpuData)));

        reff.current?.appendChild(virtualCanvas);
      });
      // const float32Data = new Float32Array(64 * 64);
      // const outputMap = await session.run(inputs);
      // const outputTensor = outputMap.values().next().value;
    })();
  }, []);
  return (
    <>
      <div ref={reff}>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
