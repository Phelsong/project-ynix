import React from "react";
import { UserSettings, Login } from "../index";
//----------------------------------------------------------------
//----------------------------------------------------------------
const Profile = () => {
  //----------------------------------------------------------------

  //----------------------------------------------------------------
  return (
    <div className="profile-container">
      Profile
      <button
        className="uk-button"
        type="button"
        uk-toggle="target: .user-settings-container"
      >
        Edit
      </button>
      <UserSettings />
    </div>
  );
};
//----------------------------------------------------------------
export default Profile;
