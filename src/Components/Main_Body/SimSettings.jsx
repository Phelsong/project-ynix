import React from "react";
import { useNavigate } from "react-router-dom";
import { ClassDropdown, PlayerInputForm, DefenderForm } from "../index";
//----------------------------------------------------------------

//----------------------------------------------------------------
const SimSettings = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  //----------------------------------------------------------------
  return (
    <div className="sim-settings-container">
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
      <button className="btn btn-primary" onClick={(e) => navTo("/Results")}>
        {" "}
        Run{" "}
      </button>
    </div>
  );
};
//----------------------------------------------------------------
export default SimSettings;
