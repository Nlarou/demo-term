import React from "react";
import { useState, useContext } from "react";
import AnalyzeContext from "../context/Context";
import { analyze } from "../context/Actions";
export default function Search() {
  const [text, setText] = useState();
  const { results, dispatch } = useContext(AnalyzeContext);

  const handleChange = (e) => {
    setText(e.target.value);
  };

  //Get the channel or the user from the search
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (text === "") {
      console.log("Enter");
    } else {
      dispatch({ type: "SET_LOADING" });
      const results = await analyze(text);
      dispatch({ type: "SET_RESULTS", payload: results });
    }
  };

  return (
    <div>
      <div>
        <h2 className="font-bold">Analyze text</h2>
      </div>
      <div className="grid grid-cols-1 xl:grid-cols-2 lg:grid-cols-2 md:grid-cols-2 mb-8 gap-8">
        <div>
          <form onSubmit={handleSubmit}>
            <div className="form-control">
              <div className="relative">
                <input
                  className="w-full pr-40 bg-gray-200 input input-lg text-black"
                  type="text"
                  placeholder="Analyze"
                  value={text}
                  onChange={handleChange}
                />
                <button
                  className="absolute top-0 right-0 rounded-l-none w-36 btn btn-lg"
                  type="submit"
                >
                  Go
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
