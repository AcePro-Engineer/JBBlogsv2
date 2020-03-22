import React, { Component } from "react";

import TextField from "../../components/genericcomponents/TextField";
import Button from "../../components/genericcomponents/Button";

import {loginUser} from "../../utils/api/handleUserOperations";

import "./styles/loginform.css";

{/*
    Purpose: Parent component handles all user login related processing.

    Date created: 2/25/2020
*/}

const textFieldSyles = {
    width: '50%',
    height: '35px',
    float: 'right',
    marginRight: '10px',
    marginBottom: '15px',
    display: 'flex',
}

const buttonStyles = {
    backgroundColor: '#008CBA',
    border: 'none',
    height: '30px',
    width: '724px',
    minWidth: 'auto'
}

class LoginForm extends Component
{
    constructor(props)
    {
        super(props);

        this.handleChange = this.handleChange.bind(this);
        this.handle_login = this.handle_login.bind(this);

        this.state = {
            username: '',
            password: '',
            requestErrorMessage: '',
            errorMessage: ''
        }
    }

    handleChange(event)
    {
        event.preventDefault();

        const value = event.target.value;
        const name = event.target.name;

        this.setState({[name]: value});
    }

    handle_login(event)
    {
        event.preventDefault();

        if(this.state.username && this.state.password)
        {
            let userObj = {
                username: this.state.username,
                password: this.state.password
            };

            loginUser(userObj, 
                res => 
                {
                    localStorage.setItem('token', res.data.token);
                    this.props.onLoginChange(this.state.username);
                    this.props.history.push("/");
                },
                err =>
                {
                    if(err != null && err.response != null)
                    {
                        this.setState({requestErrorMessage: err.message});
                        this.setState({errorMessage: err.response.data.message});
                    }
                    else
                    {
                        this.setState({errorMessage: 'An unknown error has occurred please report this issue to your system administrator.'});
                    }
                });
        }
    }

    render()
    {
        return (
            <div className="login-page">
                <div id="loginform-content">
                    <TextField controlName="username"
                            controlPlaceHolder="Username or e-mail"
                            value={this.state.username}
                            handleChange={this.handleChange}
                            customStyle={textFieldSyles}
                            id="usernameTextField"
                    />

                    <TextField controlType="password"
                            controlName="password"
                            controlPlaceHolder="Password"
                            value={this.state.password}
                            handleChange={this.handleChange}
                            customStyle={textFieldSyles}
                            id="passwordTextField"
                    />
                    <div id="buttonArea">
                        <Button buttonVariant="primary"
                                IsDisabled={false}
                                handleClick={this.handle_login}
                                label="Sign In"
                                customStyle={buttonStyles}
                                id="btn-sign-in"
                        />
                </div>
                </div>
            </div>
        )
    }
}

export default LoginForm;
