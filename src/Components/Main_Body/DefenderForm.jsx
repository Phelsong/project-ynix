import React from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown} from "../index"
//----------------------------------------------------------------
//----------------------------------------------------------------
const DefenderForm = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  //----------------------------------------------------------------
  return (
    <div className="container">
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
      </form>
    </div>
  );
};
//----------------------------------------------------------------
export default DefenderForm;
