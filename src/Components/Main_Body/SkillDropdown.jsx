import React, { useEffect, useState } from "react";
import { getClassSkillList } from "../../Requests";
//----------------------------------------------------------------
//----------------------------------------------------------------
const SkillDropdown = ({ attackerClass, setSkillChoice }) => {
  //----------------------------------------------------------------
 const [skillList, setSkillList] = useState([])
  useEffect(() => {
    async function first() {
    const skills = await getClassSkillList(attackerClass)
    setSkillList(skills),
    setSkillChoice(skills[0].class_id+.1)
  }
    first()
  }, [attackerClass]);

  //----------------------------------------------------------------
  return (
    <select type="dropdown" className="classList" onChange={ e => {
      console.log(e.target.value)
      setSkillChoice(e.target.value)}}>
      {skillList.length ? (
        skillList.map((skill) => {
          return (
            <option key={skill.skill_id} value={skill.skill_id} >
              {skill.skill_name}
            </option>
          );
        })
      ) : (
        <option value="0">Please Select a Class</option>
      )}
    </select>
  );
};
//----------------------------------------------------------------
export default SkillDropdown;
