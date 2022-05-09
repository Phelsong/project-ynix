import React, {lazy} from 'react';
import { Route, Routes } from "react-router-dom";
//----------------------------------------------------------------
import {Home} from "../index"
//----------------------------------------------------------------
const MainWrapper = () => {
//----------------------------------------------------------------




//----------------------------------------------------------------
    return (
    <div className="Main-Components">
        <Routes>
            <Route path='/' element={<Home />} />
        </Routes>
    </div>) 
}
//----------------------------------------------------------------
export default MainWrapper;