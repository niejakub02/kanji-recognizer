import {
  FC,
  ReactNode,
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";
import { InferenceSession, Tensor } from "onnxruntime-web";
import useLoaderContext from "./LoaderContext";
import { Prediction } from "@interfaces/common";
import { models } from "@components/ModelsMenu/ModelsMenu";

type ModelProviderProps = {
  children: ReactNode;
};

type ModelContext = {
  loadModel: (modelPath: string, dictPath: string) => Promise<void>;
  predict: (input: any) => Promise<void>;
  prediction: Prediction[];
  session?: InferenceSession;
};

const context = createContext({} as ModelContext);

export const ModelProvider: FC<ModelProviderProps> = ({ children }) => {
  const [session, setSession] = useState<InferenceSession>();
  const [dict, setDict] = useState<{ [key: string]: string }>({});
  const [prediction, setPrediciton] = useState<Prediction[]>([]);
  const { setIsLoading } = useLoaderContext();

  const loadDict = async (path: string) =>
    fetch(path)
      .then((response) => response.json())
      .then((json) => setDict(json));

  const loadModel = async (modelPath: string, dictPath: string) => {
    setIsLoading(true);
    try {
      setSession(await InferenceSession.create(modelPath));
      await loadDict(dictPath);
      console.log("Model loaded successfully");
    } catch (err) {
      console.log("Something went wrong while loading model");
      console.log(err);
    } finally {
      setIsLoading(false);
    }
  };

  const predict = async (input: any) => {
    if (!session) return;
    const feeds: Record<string, Tensor> = {};
    feeds[session.inputNames[0]] = input;
    const outputData = await session.run(feeds);
    const output = outputData[session.outputNames[0]];
    let arr = [...output.data] as number[];

    const arr2 = [...arr];
    for (let i = 0; i < 12; i++) {
      const index = arr.indexOf(Math.max(...arr));
      console.log(dict[index], "-", arr[index]);
      arr[index] = Number.NEGATIVE_INFINITY;
    }

    const softmax = (values: number[]) =>
      values.map(
        (v) =>
          Math.exp(v) /
          values.reduce((acc, currentValue) => acc + Math.exp(currentValue), 0)
      );

    arr = softmax([...arr2]);
    const currentPrediction: Prediction[] = [];
    for (let i = 0; i < 12; i++) {
      const index = arr.indexOf(Math.max(...arr));
      console.log(dict[index], "-", arr[index]);
      currentPrediction.push({
        literal: dict[index],
        value: arr[index],
      });
      arr[index] = Number.NEGATIVE_INFINITY;
    }
    setPrediciton(currentPrediction);
  };

  useEffect(() => {
    (async () => {
      const [model] = models;
      await loadModel(model.modelPath, model.mapObjectPath);
    })();
  }, []);

  return (
    <context.Provider value={{ loadModel, predict, prediction, session }}>
      {children}
    </context.Provider>
  );
};

export const useModelContext = () => useContext(context);

export default useModelContext;
