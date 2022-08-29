const axios = require("axios").default;
// require("dotenv").config();
import {
  getZoneInfo,
  getZoneList,
  getClassInfo,
  getClassSkillList,
} from "./get_data";
import { runCalc } from "./run";
//----------------------------------------------------------------
// axios.defaults.baseURL = "http://127.0.0.1:8000";
axios.defaults.baseURL = "https://ynix-b.herokuapp.com";
axios.defaults.headers.post["Content-Type"] = "application/json";
//----------------------------------------------------------------

export async function checkApiStatus() {
  const {data: response} = await axios
    .get(`/api`)
    .catch((err) => console.error({ "Server Status": err })); 
    if (response["Server Status"] === "You've got Py") {
      return true;
    } else {
      return false;
    }
}
//----------------------------------------------------------------
export { getZoneInfo, getZoneList, getClassInfo, getClassSkillList };
export { runCalc };
