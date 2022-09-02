import React, {useEffect} from "react";
import { checkApiStatus } from "../../../Requests";
//----------------------------------------------------------------
const Home = () => {
  //----------------------------------------------------------------
 
  useEffect(() => {
    async function checkAPI() {
      const check = await checkApiStatus()
      const status = document.querySelector("#web-status")
      if (check === true){status.innerText="Web Server is Healthy"}
      if (check === false){status.innerText="Web Server Connection Error"}
    }
    checkAPI();

  },[])


  //----------------------------------------------------------------
  return (
    <div className="Home">
      <h1>Welcome to Project_Ynix!</h1>
      <h5>Alpha Version 0.1.0</h5>
      <p className="home-body"> This is the very first build version and is far from complete!, follow the project for updates. Version 0.1.1 will include an auto updater.</p>
       <span id="web-status"> </span>
    </div>
  );
};
//----------------------------------------------------------------
export default Home;
