import React from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown} from "../index"
//----------------------------------------------------------------

//----------------------------------------------------------------
const SimSettings = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  //----------------------------------------------------------------
  return (
    <div className="sim-settings-container">
      SimSettings Attacker
      <form className="sim-settings-form">
        ap
        <input type="text" />
        aap
        <input type="text" />
        accuracy
        <input type="text" />
        accuracy rate
        <input type="text" />
        monster ap
        <input type="text" />
        kama damage
        <input type="text" />
        demi-human damage
        <input type="" />
        human damage
        <input type="text" />
        bonus critial damage
        <input type="text" />
        bonus back damage
        <input type="text" />
        bonus down damage
        <input type="text" />
        bonus air damage
        <input type="text" />
        ap combat buffs
        <input type="text" />
        ap debuffs
        <input type="text" />
        accuracy combat buffs
        <input type="text" />
        accuracy debuffs
        <input type="text" />
      </form>
      <form className="sim-settings-form">
        Defender dr
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
        Attacker - Class
       <ClassDropdown />
       Defender - PvP
       <ClassDropdown />
       <button className="btn btn-primary" onClick={e => navTo('/Results')}> Run </button>
      </form>
     
    </div>
  );
};
//----------------------------------------------------------------
export default SimSettings;
