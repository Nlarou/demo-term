import { useContext } from "react";
import Spinner from "./Spinner";
import ResultItem from "./ResultItem";
import AnalyzeContext from "../context/Context";
export default function Result() {
  const { results, loading, dispatch } = useContext(AnalyzeContext);
  if (!loading) {
    return (
      <div className="grid grid-cols-1 gap-8 xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2">
        {results?.length > 0
          ? results.map((text, i) => {
              return <ResultItem key={i} text={text} />;
            })
          : null}
      </div>
    );
  } else {
    return <Spinner />;
  }
}
