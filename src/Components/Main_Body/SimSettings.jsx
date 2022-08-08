import React, {useEffect, useState} from "react";
import { useNavigate } from "react-router-dom";
import {
  SkillDropdown,
  PlayerInputForm,
  DefenderForm,
} from "../index";
import {attackerData} from "./PlayerInputForm"
import {defenderData} from "./DefenderForm"
import { runCalc } from "../../Requests";
//----------------------------------------------------------------
const SimSettings = ({setCalcRun}) => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  const [attackerClass, setAttackerClass] = useState(1)
  const [skillChoice, setSkillChoice] = useState(null)
 
  useEffect(() => {},[attackerClass])
  //----------------------------------------------------------------
  async function RunSim() {
    attackerData.class_id = Number(attackerClass)
    const calcData = await runCalc(attackerData, defenderData, skillChoice)
    await setCalcRun(calcData)
    navTo("../Results");
  }

  //----------------------------------------------------------------
  return (
    <div className="sim-settings-container">
      <SkillDropdown attackerClass={attackerClass} setSkillChoice={setSkillChoice}/>
      <switch type="checkbox" toggle />
      <button
        className="uk-button"
        type="button"
        uk-toggle="target: .player-settings-container"
      >
        Player Input
      </button>
      <PlayerInputForm className="sim-settings-form" attackerClass={attackerClass} setAttackerClass={setAttackerClass} />
      <button
        className="uk-button"
        type="button"
        uk-toggle="target: .defender-settings-form, .class-choice-form"
      >
        Defender
      </button>
      <DefenderForm className="sim-settings-form" />
      <button className="btn btn-primary" onClick={(e) => RunSim()}>
        Run
      </button>
    </div>
  );
};
//----------------------------------------------------------------
export default SimSettings;
