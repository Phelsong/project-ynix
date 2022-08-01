import React, {useState} from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown, ZoneDropdown} from "../index"
import { getZoneList } from "../../Requests";
//----------------------------------------------------------------
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
        defender dr
        <input type="text" />
        evasion
        <input type="text" />
        dr%
        <input type="text" />
        evasion rate
        <input type="text" />
        dr combat buffs
        <input type="text" />
        evasion combat buffs
        <input type="text" />
        dr debuffs
        <input type="text" />
        evasion debuffs
        <input type="text" />
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


//change Call button to toggle