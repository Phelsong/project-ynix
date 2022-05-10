import React from 'react';
import {Link} from 'react-router-dom'

//----------------------------------------------------------------
const ControlBar = () => {
//----------------------------------------------------------------



//----------------------------------------------------------------
    return (
    <div className="control-bar-container">
        <Link to='/' uk-icon="home" className="nav-icon"/>
        <Link to='/SimSettings'  uk-icon="code" className="nav-icon"/>
        <Link to='/Results' uk-icon="happy" className="nav-icon"/>
        <Link to='/Profile' uk-icon="user" className="nav-icon"/>
    </div>)
}
//----------------------------------------------------------------
export default ControlBar;