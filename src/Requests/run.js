import axios from "axios";
//----------------------------------------------------------------
export async function runCalc() {
  const { data } = await axios
    .get(`/`)
    .catch((err) => console.log(err));
  return data;
}
