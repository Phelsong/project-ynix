import React, {lazy} from 'react';
import { Route, Routes } from "react-router-dom";
//----------------------------------------------------------------
import {Home, SimSettings, Results, Profile} from "../index"
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
            <Route path='/Profile' element={<Profile />} />
        </Routes>
    </div>) 
}
//----------------------------------------------------------------
export default MainWrapper;