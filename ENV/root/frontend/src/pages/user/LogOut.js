import React, { Component } from "react";

import { Redirect } from "react-router-dom";

import LoginForm from "../user/LoginForm";

{/*
    Purpose: Form handles all user Logout related processing.

    Date created: 3/1/2020
*/}

class LogOut extends Component 
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        const navigate = this.props.shouldRedirect;

        if(navigate === true)
        {
            return <Redirect to='/pages/user/LoginForm' component={(props) => <LoginForm {...props} onLoginChange={this.props.handleLoggedIn}/>}/>;
        }

        return (
                <div className="LogOut">

                </div>
        );
    }
}

export default LogOut;
