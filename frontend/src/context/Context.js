import { createContext, useReducer } from "react";
import AnalyzeReducer from "./Reducer";
const AnalyzeContext = createContext();

export const AnalyzeProvider = ({ children }) => {
  //Initial state
  const initialState = {
    text: [],
    results: [],
    loading: false,
  };
  //Our state and dispatch that will be able to give the current state and dispatch from the reducer
  const [state, dispatch] = useReducer(AnalyzeReducer, initialState);

  //This is the provider for our context
  return (
    <AnalyzeContext.Provider
      value={{
        ...state,
        dispatch,
      }}
    >
      {children}
    </AnalyzeContext.Provider>
  );
};

export default AnalyzeContext;
