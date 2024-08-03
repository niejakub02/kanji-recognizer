import { useRef, useCallback, forwardRef, useImperativeHandle } from 'react';
import './Canvas.scss';
import { createCanvas, drawSolidLine } from '@utils/canvasUtils';

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
      container.addEventListener('pointermove', draw);
    };

    const drawEnd = () => {
      canvasContainer.current?.removeEventListener('pointermove', draw);
    };

    const strokeFinish = () => {
      drawEnd();
      onStrokeAdd?.();
    };

    const draw = useCallback((e: MouseEvent) => {
      const canvas = canvasContainer.current
        ?.lastChild as HTMLCanvasElement | null;
      if (!canvas) return;
      const context = canvas.getContext('2d');
      const { current: container } = canvasContainer;
      if (!context || !container) return;
      const x = e.pageX - container.offsetLeft;
      const y = e.pageY - container.offsetTop;
      drawSolidLine(context, x, y);
    }, []);

    return (
      <div
        className={`canvas-container`}
        ref={canvasContainer}
        onPointerDown={drawStart}
        onPointerUp={strokeFinish}
        onPointerLeave={drawEnd}
      ></div>
    );
  }
);

export default Canvas;