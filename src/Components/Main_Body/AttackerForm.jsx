import React, {useState} from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown} from "../index"
//----------------------------------------------------------------
const attackerData = {
  "ap": 0,
  "aap": 0, 
  "acc": 0, 
  "acc_rate": 0, 
  "crit_rate": 0, 
  "monster_ap": 0, 
  "kama_damage": 0, 
  "demi_damage": 0, 
  "human_damage": 0, 
  "other_damage": 0, 
  "crit_damage": 0, 
  "back_damage": 0 , 
  "down_damage": 0, 
  "air_damage": 0, 
  "ap_combat_buffs": 0, 
  "crit_combat_buffs": 0, 
  "ap_debuffs": 0, 
  "acc_combat_buffs": 0, 
  "acc_debuffs": 0, 
  "human_damage_debuffs": 0
}
//----------------------------------------------------------------
const PlayerInputForm = ({attackerClass, setAttackerClass}) => {
  //----------------------------------------------------------------


  //----------------------------------------------------------------
  return (
    <div className="attacker-settings-container">
      Attacker - Class
       <ClassDropdown setAttackerClass={setAttackerClass}/>
      <form className="attacker-settings-form">
        {Object.keys(attackerData).map(item => { 
                return <>
                <label className="attacker-settings-label">{item}</label>
                <input type="text" onChange={(e) => {
                  attackerData[item] = Number(e.target.value)
                  }} />
                </>
        })}
      </form>
    </div>
  );
};
//----------------------------------------------------------------
export default PlayerInputForm;
export { attackerData }