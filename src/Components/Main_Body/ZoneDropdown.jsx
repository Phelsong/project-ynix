import React, {useEffect, useState} from "react";
import { getZoneList } from "../../Requests";
//----------------------------------------------------------------
//----------------------------------------------------------------
const ZoneDropdown = ({zoneList}) => {
  //----------------------------------------------------------------

  //----------------------------------------------------------------
  return (
    <select type="dropdown" className="classList" onChange={e => e.preventDefault}>
      {zoneList.length
        ? zoneList.map(zone => (
            <option key={zone.zone_id}>
            {zone.zone_name}
            </option>
          ))
        : null}
    </select>
  );
};
//----------------------------------------------------------------
export default ZoneDropdown;
