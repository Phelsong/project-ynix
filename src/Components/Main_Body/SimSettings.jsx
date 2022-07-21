import React from "react";
import { useNavigate } from "react-router-dom";
import {ClassDropdown, PlayerInputForm, DefenderForm} from "../index"
//----------------------------------------------------------------

//----------------------------------------------------------------
const SimSettings = () => {
  //----------------------------------------------------------------
  const navTo = useNavigate();
  //----------------------------------------------------------------
  return (
    <div className="sim-settings-container">
      <h1> Simulation Settings</h1>
      <switch type="checkbox" toggle/>
      <PlayerInputForm className="sim-settings-form" />
      <DefenderForm className="sim-settings-form" />
      <button className="btn btn-primary" onClick={e => navTo('/Results')}> Run </button>
    </div>
  );
};
//----------------------------------------------------------------
export default SimSettings;
