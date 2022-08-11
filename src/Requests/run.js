import axios from "axios";
//----------------------------------------------------------------
export async function runCalc(attacker, defender, skillChoice) {
  const { data: response} = await axios.put(`/basic_calc`, {"attacker_in" : attacker, "defender_in":  defender, "skill_id": [skillChoice] })
  .catch((err) => console.log(err));
  return response;
}
