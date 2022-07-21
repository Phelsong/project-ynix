import axios from 'axios';
//----------------------------------------------------------------
const url = 'http://127.0.0.1:8000'
//----------------------------------------------------------------
export async function checkAPI() {
    try {
      const { data } = await axios.get(`${url}/api`);
      return data;
    } 
    catch (err) {
      console.error(err);
      return { healthy: false };
    }
  }