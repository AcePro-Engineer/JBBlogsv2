import React, { Component } from "react";
import { Route, NavLink, HashRouter } from "react-router-dom";

import Home from "./pages/home/Home";
import Contact from "./pages/contact/Contact";
import About from "./pages/about/About";
import PostSubmitPage from "./pages/postsubmit/PostSubmitForm";
import Post from "./pages/posts/Post";
import LoginForm from "./pages/user/LoginForm";
import SignUpForm from "./pages/user/SignUpForm";
import LogOut from "./pages/user/LogOut";

import {userAlreadyLoggedIn} from "../src/utils/api/handleUserOperations";

import "./App.css";

{/*
    Purpose: Main "wrapper" page for all components.
*/}

{/* 
    DEVELOPER NOTE: Using an inline CSS style in order
                    to ensure the necessary styles
                    are applied to my custom components.
                    For some reason my custom components
                    cannot be styled by an external style
                    sheet. I will revisit this issue
                    at a later time.
*/}

const navLinkStyles = {
  display: 'block',
  padding: '10px',
  textDecoration: 'none'
}
 
class App extends Component 
{ 
    constructor(props)
    {
        super(props);

        this.handleUserLoggedIn = this.handleUserLoggedIn.bind(this);
        this.handleUserLogOut = this.handleUserLogOut.bind(this);

        this.state = {
          logged_in: localStorage.getItem('token') ? true : false,
          username: ''
        }
    }

    componentDidMount()
    {
       
    }

    handleUserLoggedIn(username)
    {
        let is_logged_in = localStorage.getItem('token') != null ? true : false;

        this.setState({logged_in: is_logged_in,
                       username: username});
    }

    handleUserLogOut(event)
    {
        localStorage.removeItem('token');
        this.setState({logged_in: false, 
                       username: ''});
    }

    getNavBar()
    {
        {/*
            Purpose: Function conditionally generates a navigation bar based on
                     rather a user is logged into the site.
        */}

        
       if(this.state.logged_in === true)
       {
            return (
                      <ul class="topnav-navbar">
                        <li class="topnav">
                            <NavLink class="topnav-link" 
                                    to="/"  
                                    style={navLinkStyles}
                            >
                                Home
                            </NavLink>
                        </li>
                        <li class="topnav">
                            <NavLink class="topnav-link" 
                                    to="/pages/about/About"  
                                    style={navLinkStyles}
                            >
                                About
                            </NavLink>
                        </li>
                        <li class="topnav">
                            <NavLink class="topnav-link" 
                                    to="/pages/contact/Contact" 
                                    style={navLinkStyles}
                              >
                                Contact
                              </NavLink>
                        </li>
                        <li class="topnav" id="topnav-sign-out">
                            <NavLink class="topnav-link" 
                                    to="/pages/user/LogOut" 
                                    style={navLinkStyles} 
                                    onClick={this.handleUserLogOut}
                            >
                                Sign Out
                            </NavLink>
                        </li>
                        <li class="topnav" id="topnav-create-post">
                            <NavLink class="topnav-link" 
                                    to="/pages/postsubmit/PostSubmitForm" 
                                    style={navLinkStyles}
                            >
                                Create Post
                            </NavLink>
                        </li>
                    </ul>
            );
       }
       else
       {
          return (
            <ul class="topnav-navbar">
                  <li class="topnav">
                      <NavLink class="topnav-link" 
                                to="/"  
                                style={navLinkStyles}
                      >
                          Home
                      </NavLink>
                  </li>
                  <li class="topnav">
                      <NavLink class="topnav-link" 
                                to="/pages/about/About"  
                                style={navLinkStyles}
                      >
                          About
                      </NavLink>
                  </li>
                  <li class="topnav">
                      <NavLink class="topnav-link" 
                                to="/pages/contact/Contact" 
                                style={navLinkStyles}
                        >
                          Contact
                        </NavLink>
                  </li>
                  <li class="topnav" id="topnav-sign-in">
                      <NavLink class="topnav-link" 
                                to="/pages/user/LoginForm" 
                                style={navLinkStyles}
                      >
                          Sign In
                      </NavLink>
                  </li>
            </ul>
          );
       }
    }

    render() 
    {

      let navigationBar = this.getNavBar();

      return (
                <HashRouter>
                  <div>
                    
                    <h1 id="page-title">JB's Blogs</h1>

                    <ul class="topnav-navbar">
                        {navigationBar}
                    </ul>

                    <div className="maincontent">
                      <Route exact path="/" component={Home}/>
                      <Route path="/pages/contact/Contact" component={Contact}/>
                      <Route path="/pages/about/About" component={About}/>
                      <Route path="/pages/postsubmit/PostSubmitForm" component={(props) => <PostSubmitPage {...props} username={this.state.username} />}/>
                      <Route path="/pages/posts/Post/" component={Post}/>
                      <Route path="/pages/user/LoginForm" component={(props) => <LoginForm {...props} onLoginChange={this.handleUserLoggedIn}/>} />
                      <Route path="/pages/user/LogOut" component={(props) => <LogOut {...props} handleLoggedIn={this.handleUserLoggedIn} shouldRedirect={true}/>} />
                      <Route path="/pages/user/SignUpForm" component={SignUpForm}/>
                    </div>

                    <footer>
                      <h2>THIS IS THE FOOTER</h2>
                    </footer>

                  </div>
                </HashRouter>
      );
    }
}

export default App;
