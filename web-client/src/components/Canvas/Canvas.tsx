import { useRef, useCallback, forwardRef, useImperativeHandle } from "react";
import "./Canvas.scss";
import { createCanvas, drawSolidLine } from "@utils/canvasUtils";
import { isMobile } from "react-device-detect";

interface CanvasProps {
  onStrokeAdd?: () => void;
}

export const Canvas = forwardRef<HTMLDivElement, CanvasProps>(
  ({ onStrokeAdd }, ref) => {
    const canvasContainer = useRef<HTMLDivElement>(null);

    useImperativeHandle(
      ref,
      () => canvasContainer.current as HTMLDivElement,
      []
    );

    const drawStart = () => {
      const { current: container } = canvasContainer;
      if (!container) return;
      container.append(createCanvas());
      container.addEventListener(isMobile ? "touchmove" : "mousemove", draw);
    };

    const drawEnd = () => {
      canvasContainer.current?.removeEventListener(
        isMobile ? "touchmove" : "mousemove",
        draw
      );
    };

    const strokeFinish = () => {
      drawEnd();
      onStrokeAdd?.();
    };

    const draw = useCallback((e: MouseEvent | TouchEvent) => {
      const canvas = canvasContainer.current
        ?.lastChild as HTMLCanvasElement | null;
      if (!canvas) return;
      const context = canvas.getContext("2d");
      const { current: container } = canvasContainer;
      if (!context || !container) return;
      const clientX = isMobile
        ? (e as TouchEvent).touches[0].pageX
        : (e as MouseEvent).pageX;
      const clientY = isMobile
        ? (e as TouchEvent).touches[0].pageY
        : (e as MouseEvent).pageY;
      const x = clientX - container.offsetLeft;
      const y = clientY - container.offsetTop;
      drawSolidLine(context, x, y);
    }, []);

    const handlers = isMobile
      ? {
          onTouchStart: drawStart,
          onTouchEnd: strokeFinish,
        }
      : {
          onMouseDown: drawStart,
          onMouseUp: strokeFinish,
          onMouseLeave: drawEnd,
        };

    return (
      <div
        className="canvas-container"
        ref={canvasContainer}
        {...handlers}
      ></div>
    );
  }
);

export default Canvas;
