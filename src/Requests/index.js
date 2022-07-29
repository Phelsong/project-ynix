import axios from 'axios';
require("dotenv").config();
import {getZoneInfo} from"./get_data"
//----------------------------------------------------------------
const apiUrl = process.env.REACT_APP_API_URL;
//----------------------------------------------------------------

export async function checkAPI() {
  const {
    data
  } = await axios.get(`${url}/api`)
    .then(res =>
      res.data)
    .catch(err => console.error(err))
}
//----------------------------------------------------------------
export {getZoneInfo}