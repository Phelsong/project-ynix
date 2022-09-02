import React from "react";
import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons.min.js';
UIkit.use(Icons);
import "./Style/index.css"
import {MainWrapper, ControlBar} from "./Components"
//----------------------------------------------------------------
const App = () => {
//----------------------------------------------------------------


//----------------------------------------------------------------
    return(
        <>  
            <ControlBar />
            <MainWrapper/>
        </>
    )
}
//----------------------------------------------------------------
export default App;