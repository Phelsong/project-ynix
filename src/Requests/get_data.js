import axios from "axios";
//----------------------------------------------------------------
export async function getZoneInfo(zoneId = 33) {
  const { data } = await axios
    .get(`/zones/${zoneId}/info`)
    .catch((err) => console.log(err));
  return data;
}
//----------------------------------------------------------------
export async function getZoneList() {
  const { data } = await axios.get(`/zones`).catch((err) => console.log(err));
  return data;
}
//----------------------------------------------------------------
export async function getClassInfo(classId) {
  const { data } = await axios
    .get(`/class/${classId}`)
    .catch((err) => console.log(err));
  return data;
}
//----------------------------------------------------------------
export async function getClassSkillList(classId) {
  //!!route not implementated yet!!
  const { data } = await axios
    .get(`/class/${classId}/skill_list`)
    .catch((err) => console.log(err));
  return data;
}
//----------------------------------------------------------------
