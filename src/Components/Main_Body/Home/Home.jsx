import React from "react";
import { checkApiStatus } from "../../../Requests";
//----------------------------------------------------------------
const Home = () => {
  //----------------------------------------------------------------
  async function checkAPI() {
    await checkApiStatus()
  }
  //----------------------------------------------------------------
  return (
    <div className="Home">
      <h1>Welcome to Project_Ynix!</h1>
      <button onClick={() => checkAPI()} style={{ width: 50, height: 50, alignSelf: 'flex-end', margin: 1000}}>Check </button>
    </div>
  );
};
//----------------------------------------------------------------
export default Home;
