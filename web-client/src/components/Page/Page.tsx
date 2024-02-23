import { FC, ReactNode } from "react";
import "./Page.scss";
import { Link } from "react-router-dom";

interface PageProps {
  children: ReactNode;
  center?: boolean;
}
export const Page: FC<PageProps> = ({ children, center }) => {
  return (
    <div className={`page ${center ? "page--center" : ""}`}>
      <div className="github-ref">
        <Link to="https://github.com/niejakub02/kanji-recognizer">
          <img
            src="/kanji-recognizer/github-mark-white.svg"
            className="github-ref__logo"
          />
        </Link>
      </div>
      {children}
    </div>
  );
};

export default Page;
