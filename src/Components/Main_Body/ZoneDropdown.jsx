import React, { useEffect, useState } from "react";
import { getZoneList } from "../../Requests";
//----------------------------------------------------------------
//----------------------------------------------------------------
const ZoneDropdown = ({ zoneList, defenderData }) => {
  //----------------------------------------------------------------

  //----------------------------------------------------------------
  return (
    <select
      type="dropdown"
      className="classList"
      onChange={e => {
        // need to rewrite later to accommodate other stats
        e.preventDefault;
        const here = e.target.value
        defenderData.dr = zoneList[here]['zone_dr']
        defenderData.evasion = zoneList[here]['zone_evasion']
        defenderData.species = zoneList[here]['mob_type']
      }}
    >
      {zoneList.length
        ? zoneList.map((zone, i) => (
            <option key={zone.zone_id} value={i}>{zone.zone_name}</option>
          ))
        : null}
    </select>
  );
};
//----------------------------------------------------------------
export default ZoneDropdown;
