import axios from "axios";

{/*
    Purpose: Script handles all user related operations.

    Date created: 2/25/2020
 */}

 {/* 
     Function sends post request to backend api
     in order to handle user login operation. 
*/}
 export function loginUser(user, callBack, errorCallBack)
 {
    const loginURL = 'http://127.0.0.1:8000/token-auth/';

    axios.post(loginURL, user)
        .then(response => {
            if(callBack != null)
            {
                callBack(response);
            }
        })
        .catch(error => {
            if(errorCallBack != null)
            {
                errorCallBack(error);
            }
        })
 }

 {/*
    Functions sends post request to backend api
    in order to handle user sign up operation.
*/}
 export function signUpUser(user, callBack, errorCallBack)
 {
    const signUpURL = 'http://127.0.0.1:8000/users/';

    axios.post(signUpURL, user)
        .then(response => {
            if(callBack != null)
            {
                callBack(response);
            }
    })
    .catch(error => {
            if(errorCallBack != null)
            {
                errorCallBack(error);
            }
    })
 }

 {/*
    Function sends a header request to handle users that have
    already been logged into the site.
*/}
 export function userAlreadyLoggedIn(user, callBack, errorCallBack)
 {
    const currentUserURL = 'http://127.0.0.1:8000/currentuser/';

    {/* TODO: CHANGE TO HEADER REQUEST ASAP. */}
    axios.post(currentUserURL, user)
        .then(response => {
            if(callBack != null)
            {
                callBack(response);
            }
    })
    .catch(error => {
            if(errorCallBack != null)
            {
                errorCallBack(error);
            }
    })
 }

{/*
    Function sends post request to backend api
    in order to handle user log out operation.
*/}
export function logOutUser(user, callBack, errorCallBack)
{
   {/* TODO: ADD USER LOG OUT REQUEST LOGIC, IF APPLICABLE. */}
}
