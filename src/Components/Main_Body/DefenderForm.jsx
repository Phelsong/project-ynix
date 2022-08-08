import React, {useState} from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown, ZoneDropdown} from "../index"
import { getZoneList } from "../../Requests";
//----------------------------------------------------------------
const defenderData = {
  "dr": 0,
  "dr_rate": 0,
  "evasion": 0,
  "evasion_rate": 0,
  "dr_combat_buffs" : 0,
  "dr_debuffs": 0,
  "evasion_combat_buffs": 0,
  "evasion_debuffs": 0,
  "class_id": 0,
  "species" : 0,
  // species : 100 = PvE
}
//----------------------------------------------------------------
const DefenderForm = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  const [zoneList, setZoneList] = useState([])

async function handleCall() {
  const temp = await getZoneList()
  setZoneList(temp)
}

  //----------------------------------------------------------------
  return (
    <div className="defender-container">
      <form className="defender-settings-form">
      {Object.keys(defenderData).map(item => { 
                return <>
                <label>{item}</label>
                <input type="text" onChange={(e) => {
                  defenderData[item] = Number(e.target.value)
                  }}
                  />
                </>
              })}
      </form>
      <form className="class-choice-form">
        Defender - PvP
        <ClassDropdown />
        PvE
        <ZoneDropdown  zoneList={zoneList}/>
        <button onClick={e => {e.preventDefault(); handleCall()}}> get list </button>
      </form>
    </div>
  );
};
//----------------------------------------------------------------
export default DefenderForm;
export { defenderData }

//change Call button to toggle