import {
  FC,
  ReactNode,
  // useState
} from "react";
import "./Page.scss";

interface PageProps {
  children: ReactNode;
  center?: boolean;
}
export const Page: FC<PageProps> = ({ children, center }) => {
  // const [r, sr] = useState<number>(0);
  return (
    <div
      className={`page ${center ? "page--center" : ""}`}
      // key={r}
    >
      {children}
      {/* <button
        onClick={() => {
          sr((r) => r + 1);
        }}
      ></button> */}
    </div>
  );
};

export default Page;
