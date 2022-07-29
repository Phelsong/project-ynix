import React from "react";
import { getZoneInfo } from "../../../Requests";
//----------------------------------------------------------------
const Home = () => {
  //----------------------------------------------------------------

  //----------------------------------------------------------------
  return (
    <div className="Home">
      <h1>Welcome to Project_Ynix!</h1>
      <button onClick={ () => {console.log(getZoneInfo());} } > </button>
    </div>
  );
};
//----------------------------------------------------------------
export default Home;
