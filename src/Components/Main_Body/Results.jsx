import React from 'react';
//----------------------------------------------------------------
//----------------------------------------------------------------
const Results = ({calcRun}) => {
//----------------------------------------------------------------

//----------------------------------------------------------------
    return (
    <div className="results-container">
        Results
    <progress className="uk-progress" value="50" max="100"></progress>
    {calcRun ? <span className="results-DUMP"> {JSON.stringify(calcRun)} </span> : null}
    <span className="uk-label uk-label-warning">Error</span>
    <span className="uk-label uk-label-success">Success!</span>
    </div>) 
}
//----------------------------------------------------------------
export default Results;

