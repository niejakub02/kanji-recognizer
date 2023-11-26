import {
  FC,
  ReactNode,
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";
import { InferenceSession, Tensor } from "onnxruntime-web";

type ModelProviderProps = {
  children: ReactNode;
};

type ModelContext = {
  loadModel: (path: string) => void;
  predict: (input: any) => void;
};

const context = createContext({} as ModelContext);

export const ModelProvider: FC<ModelProviderProps> = ({ children }) => {
  const [session, setSession] = useState<InferenceSession>();

  const loadModel = async (path: string) =>
    setSession(await InferenceSession.create(path));

  const predict = async (input: any) => {
    if (!session) return;
    console.log(input);
    const feeds: Record<string, Tensor> = {};
    feeds[session.inputNames[0]] = input;
    const outputData = await session.run(feeds);
    const output = outputData[session.outputNames[0]];
    const arr = [...output.data] as number[];
    console.log(arr.indexOf(Math.max(...arr)));
  };

  useEffect(() => {
    (async () => {
      try {
        await loadModel("./../../model_1_7.onnx");
        console.log("Model loaded successfully");
      } catch (err) {
        console.log("Something went wrong while loading model");
        console.log(err);
      }
    })();
  }, []);

  return (
    <context.Provider value={{ loadModel, predict }}>
      {children}
    </context.Provider>
  );
};

export const useModelContext = () => useContext(context);

export default useModelContext;
