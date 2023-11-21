import {
  FC,
  ReactNode,
  RefObject,
  createContext,
  useRef,
  useContext,
} from "react";

type CanvasControlContext = {
  ref: RefObject<HTMLDivElement>;
  reset: () => void;
  undo: () => void;
  save: () => void;
};

type CanvasControlProviderProps = {
  children: ReactNode;
};

const context = createContext<CanvasControlContext>({} as CanvasControlContext);
// const ref = createRef<HTMLDivElement>();

export const CanvasControlProvider: FC<CanvasControlProviderProps> = ({
  children,
}) => {
  const ref = useRef<HTMLDivElement>(null);

  const reset = () => {
    if (ref.current) {
      ref.current.innerHTML = "";
    }
  };

  const undo = () => ref.current?.lastChild?.remove();

  const save = () => {};

  return (
    <context.Provider value={{ ref, reset, undo, save }}>
      {children}
    </context.Provider>
  );
};

export const useCanvasControlContext = () => useContext(context);

export default useCanvasControlContext;
