import axios from "axios";
const API_URL = "/api/";

//Create new Ticket
export const analyze = async (text) => {
  const response = await axios.post(API_URL + "analyze", { text: text });
  return response.data;
};
