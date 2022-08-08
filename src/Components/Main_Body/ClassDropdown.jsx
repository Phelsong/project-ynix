import React from "react";
//----------------------------------------------------------------
//----------------------------------------------------------------
const ClassDropdown = ({setAttackerClass}) => {
  //----------------------------------------------------------------
  function handle(e){
    e.preventDefault();
    setAttackerClass(e.target.value);
  }
  //----------------------------------------------------------------
  return (
    <select type="dropdown" className="classList" onChange={e => handle(e)}>
      <option value="1">Warrior</option>
      <option value="2">Ranger</option>
      <option value="3">Sorceress</option>
      <option value="4">Berserker</option>
      <option value="5">Tamer</option>
      <option value="6">Valkyrie</option>
      <option value="7">Wizard</option>
      <option value="8">Witch</option>
      <option value="9">Musa</option>
      <option value="10">Maewha</option>
      <option value="11">Kunoichi</option>
      <option value="12">Ninja</option>
      <option value="13">Dark Knight</option>
      <option value="14">Striker</option>
      <option value="15">Mystic</option>
      <option value="16">Lahn</option>
      <option value="17">Archer</option>
      <option value="18">Shai</option>
      <option value="19">Guardian</option>
      <option value="20">Hashashin </option>
      <option value="21">Nova</option>
      <option value="22">Sage</option>
      <option value="23">Corsair</option>
      <option value="24">Drakania</option>
    </select>
  );
};
//----------------------------------------------------------------
export default ClassDropdown;
