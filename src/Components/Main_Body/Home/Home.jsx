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
      <p className="home-body"> Someday I might right some stuff here... maybe a link to a wiki or some such. </p>
       <span id="web-status"> </span>
    </div>
  );
};
//----------------------------------------------------------------
export default Home;
