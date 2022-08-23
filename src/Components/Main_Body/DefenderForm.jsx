import React, {useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import {DefenderClassDropdown, ZoneDropdown} from "../index"
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
  //class_id : 100 = PvE
}
//----------------------------------------------------------------
const DefenderForm = ({setDefenderClass, pveOrPvp, setPveOrPvp}) => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  const [zoneList, setZoneList] = useState([])

useEffect(() => {
  if(!zoneList.length)
  {handleCall()}
}, [pveOrPvp])



async function handleCall() {
  const temp = await getZoneList()
  setZoneList(temp)
}

async function handleReset() {
  //rewrite as class instance method instead
    defender.dr = 0
    defender.dr_rate = 0
    defender.evasion = 0
    defender.evasion_rate = 0
    defedner.dr_combat_buffs = 0
    defender.dr_debuffs = 0
    defender.evasion_combat_buffs = 0
    defender.evasion_debuffs = 0
    defender.class_id =  100
    defender.species = 0
    //class_id : 100 = PvE
  
}

  //----------------------------------------------------------------
  return (
    <div className="defender-container">
       {/* __________________________________________________ */}
      <form className="defender-settings-form" onSubmit={()=> handleReset()}> 

        { pveOrPvp ? <DefenderClassDropdown defenderData={defenderData} setDefenderClass={setDefenderClass} pveOrPvp={pveOrPvp}/>  : <ZoneDropdown  zoneList={zoneList} defenderData={defenderData}/>
        }
        <input type="checkbox" onMouseDown={ e => 
        {e.preventDefault()
          if(pveOrPvp === false)
          { setPveOrPvp(true)}
          else{ setPveOrPvp(false)
          defenderData.class_id = 100}
          handleReset()
          }}></input>
      </form>
      {/* __________________________________________________ */}
      <form className="defender-form">
        {Object.keys(defenderData).map((item) => {
          return (
            <>
              <label>{item}</label>
              <input
                type="text"
                onChange={(e) => {
                  defenderData[item] = Number(e.target.value);
                }}
              />
            </>
          );
        })}
      </form>
      {/* __________________________________________________ */}
    </div>
  );
};
//----------------------------------------------------------------
export default DefenderForm;
export { defenderData }

//change Call button to toggle