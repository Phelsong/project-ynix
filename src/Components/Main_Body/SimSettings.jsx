import React, {useState} from "react";
import { useNavigate } from "react-router-dom";
import {
  SkillDropdown,
  PlayerInputForm,
  DefenderForm,
} from "../index";
//----------------------------------------------------------------
const SimSettings = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
 
  //----------------------------------------------------------------
  async function RunSim() {
    navTo("./Results.jsx");
  }

  //----------------------------------------------------------------
  return (
    <div className="sim-settings-container">
      <SkillDropdown />
      <switch type="checkbox" toggle />
      <button
        className="uk-button"
        type="button"
        uk-toggle="target: .player-settings-container"
      >
        Player Input
      </button>
      <PlayerInputForm className="sim-settings-form" />
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
