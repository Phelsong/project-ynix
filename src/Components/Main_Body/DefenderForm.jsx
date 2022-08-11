import React, {useState, useEffect} from "react";
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
  const [pveOrPvp, setPveOrPvp] = useState(false)

useEffect(() => {
  if(!zoneList.length)
  {handleCall()}
}, [pveOrPvp])



async function handleCall() {
  const temp = await getZoneList()
  setZoneList(temp)
}

async function handleSubmit() {
  
}

  //----------------------------------------------------------------
  return (
    <div className="defender-container">
      <form className="defender-settings-form" onSubmit={()=> handleSubmit()}> 

        { pveOrPvp ? <ClassDropdown defenderData={defenderData} />  : <ZoneDropdown  zoneList={zoneList}/>
        }
        <input type="checkbox" onMouseDown={ e => 
        {e.preventDefault()
          if(pveOrPvp === false)
          { setPveOrPvp(true)}
          else{ setPveOrPvp(false)}
          }}></input>
      </form>
    </div>
  );
};
//----------------------------------------------------------------
export default DefenderForm;
export { defenderData }

//change Call button to toggle