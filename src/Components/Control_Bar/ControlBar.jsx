import React from 'react';
import {Link} from 'react-router-dom'
//----------------------------------------------------------------
const ControlBar = () => {
//----------------------------------------------------------------



//----------------------------------------------------------------
    return (
    <div className="control-bar-container">
        <Link to='/' className="uk-button uk-button-default">Home</Link>
        <Link to='/SimSettings' className="uk-button uk-button-default">SimSettings</Link>
        <Link to='/Results' className="uk-button uk-button-default">Results</Link>
    </div>)
}
//----------------------------------------------------------------
export default ControlBar;