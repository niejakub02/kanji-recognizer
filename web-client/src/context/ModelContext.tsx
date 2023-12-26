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
    console.log(input);
    const feeds: Record<string, Tensor> = {};
    feeds[session.inputNames[0]] = input;
    const outputData = await session.run(feeds);
    const output = outputData[session.outputNames[0]];
    let arr = [...output.data] as number[];
    // console.log(arr);
    const arr2 = [...arr];
    // for (let i = 0; i < 10; i++) {
    //   const index = arr.indexOf(Math.max(...arr));
    //   console.log(dict[index], "-", arr[index]);
    //   arr[index] = Number.NEGATIVE_INFINITY;
    // }
    function softmax(arr: number[]) {
      return arr.map(function (value) {
        return (
          Math.exp(value) /
          arr
            .map(function (y /*value*/) {
              return Math.exp(y);
            })
            .reduce(function (a, b) {
              return a + b;
            })
        );
      });
    }

    arr = softmax([...arr2]);
    const currentPrediction: Prediction[] = [];
    for (let i = 0; i < 10; i++) {
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
      await loadModel("./../../model_1_24.onnx", "./../../model_1_24.json");
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
