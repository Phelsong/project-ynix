import axios from 'axios';
// axios.defaults.baseURL = '127.0.0.1:8000';
// axios.defaults.headers.post['Content-Type'] = 'application/json';
//----------------------------------------------------------------
export async function getZoneInfo(zoneId=33) {
    const {data} = await axios.get(`/zones/${zoneId}/info`)
    .catch(err => console.log(err))
}