import React, {lazy} from 'react';
import { Route, Routes } from "react-router-dom";
//----------------------------------------------------------------
import {Home, SimSettings, Results} from "../index"
//----------------------------------------------------------------
const MainWrapper = () => {
//----------------------------------------------------------------




//----------------------------------------------------------------
    return (
    <div className="Main-Components">
        <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/SimSettings' element={<SimSettings />} />
            <Route path='/Results' element={<Results />} />
        </Routes>
    </div>) 
}
//----------------------------------------------------------------
export default MainWrapper;