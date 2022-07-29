import axios from 'axios';
//----------------------------------------------------------------
export async function getZoneInfo(zoneId) {
    await axios.get(`${apiUrl}/zones/:${zoneId}`)
    .then(res => res.data)
    .catch(err => console.log(err))
}
  