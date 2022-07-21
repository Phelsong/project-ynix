import React from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown} from "../index"
//----------------------------------------------------------------
//----------------------------------------------------------------
const PlayerInputForm = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  //----------------------------------------------------------------
  return (
    <div className="player-settings-container">
      Attacker - Class
       <ClassDropdown />
      <form className="player-settings-form">
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
    </div>
  );
};
//----------------------------------------------------------------
export default PlayerInputForm;
