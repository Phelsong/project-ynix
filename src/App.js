import React from "react";
import UIkit from 'uikit';
import Icons from 'uikit/dist/js/uikit-icons.min.js';
UIkit.use(Icons);
import "./Style/index.css"
import {Main, ControlBar} from "./Components"
//----------------------------------------------------------------
const App = () => {
//----------------------------------------------------------------


//----------------------------------------------------------------
    return(
        <>  
            <ControlBar />
            <Main/>
        </>
    )
}
//----------------------------------------------------------------
export default App;