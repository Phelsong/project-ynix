import React, {lazy, useState} from 'react';
import { Route, Routes } from "react-router-dom";
//----------------------------------------------------------------
import {Home, SimSettings, Results, Profile} from "./index"
//----------------------------------------------------------------
const MainWrapper = () => {
//----------------------------------------------------------------
const [calcRun, setCalcRun] = useState(null)
//----------------------------------------------------------------
    return (
    <div className="Main-Components">
        <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/SimSettings' element={<SimSettings setCalcRun={setCalcRun} />} />
            <Route path='/Results' element={<Results calcRun={calcRun} />} />
            <Route path='/Profile' element={<Profile />} />
        </Routes>
    </div>) 
}
//----------------------------------------------------------------
export default MainWrapper;