const AnalyzeReducer = (state, action) => {
  switch (action.type) {
    case "SET_TEXT":
      return {
        ...state,
        text: action.payload,
        loading: false,
      };
    case "SET_RESULTS":
      return {
        ...state,
        results: action.payload,
        loading: false,
      };
    case "SET_LOADING":
      return {
        ...state,
        loading: true,
      };
    case "GET_LOADING":
      return {
        ...state,
        loading: action.payload,
      };
    case "GET_TEXT":
      return {
        ...state,
        text: action.payload,
        loading: false,
      };

    default:
      return state;
  }
};

export default AnalyzeReducer;
