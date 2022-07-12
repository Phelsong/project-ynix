import React from "react";
//----------------------------------------------------------------
//----------------------------------------------------------------
const SimSettings = () => {
  //----------------------------------------------------------------

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
      <form className="sim-settings">
        {/* This probably needs to be broken out into a seperate component, revisit latter **** */}
        Attacker - Class
        <select type="dropdown">
          <option value="1">Warrior</option>
          <option value="2">Ranger</option>
          <option value="3">Sorceress</option>
          <option value="4">Berserker</option>
          <option value="5">Tamer</option>
          <option value="6">Musa</option>
          <option value="7">Maewha</option>
          <option value="8">Valkyrie</option>
          <option value="9">Kunoichi</option>
          <option value="10">Ninja</option>
          <option value="11">Wizard</option>
          <option value="12">Witch</option>
          <option value="13">Mystic</option>
          <option value="14">Striker</option>
          <option value="15">Lahn</option>
          <option value="16">Archer</option>
          <option value="17">Dark Knight</option>
          <option value="18">Shai</option>
          <option value="19">Guardian</option>
          <option value="20">Hashashin </option>
          <option value="21">Nova</option>
          <option value="22">Sage</option>
          <option value="23">Corsair</option>
          <option value="24">Drakania</option>
        </select>
      </form>

    </div>
  );
};
//----------------------------------------------------------------
export default SimSettings;
