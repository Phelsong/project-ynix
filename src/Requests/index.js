const axios = require('axios').default;
// require("dotenv").config();
import {
  getZoneInfo
} from "./get_data"
//----------------------------------------------------------------
axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.headers.post['Content-Type'] = 'application/json';
//----------------------------------------------------------------

export async function checkApiStatus() {
  const response = await axios.get(`/api`)
    .catch(err => console.error(err))
  console.log(response.data)
}
//----------------------------------------------------------------
export {
  getZoneInfo
}