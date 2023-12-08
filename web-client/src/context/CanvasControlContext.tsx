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
  getCompoundImage: () => HTMLCanvasElement | null;
};

type CanvasControlProviderProps = {
  children: ReactNode;
};

const context = createContext<CanvasControlContext>({} as CanvasControlContext);

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

  const save = () => {
    const virtualCanvas = getCompoundImage();

    if (!virtualCanvas) return;
    const link = document.createElement("a");
    link.download = `${crypto.randomUUID()}.png`;
    link.href = virtualCanvas.toDataURL();
    link.click();
  };

  const getCompoundImage = () => {
    if (!ref.current) return null;
    const virtualCanvas = document.createElement("canvas");
    virtualCanvas.height = 64;
    virtualCanvas.width = 64;
    const virtualCtx = virtualCanvas.getContext("2d");

    if (!virtualCtx) return null;
    virtualCtx.fillStyle = "black";
    virtualCtx.fillRect(0, 0, virtualCanvas.width, virtualCanvas.height);
    const atomicCanvas = [...ref.current.children] as HTMLCanvasElement[];

    for (const canvas of atomicCanvas) {
      virtualCtx.drawImage(canvas, 0, 0, 64, 64);
    }
    return virtualCanvas;
  };

  return (
    <context.Provider value={{ ref, reset, undo, save, getCompoundImage }}>
      {children}
    </context.Provider>
  );
};

export const useCanvasControlContext = () => useContext(context);

export default useCanvasControlContext;
