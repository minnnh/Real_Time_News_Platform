import React from 'react';
import Auth from '../Auth/Auth';
// import { BrowserRouter as Router } from 'react-router-dom'
import { Route, Redirect } from 'react-router'
import { Link } from 'react-router-dom'
// import { Route, Redirect } from 'react-router'
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import './Base.css'

const Base = ({ children }) => (
    <div>
        <nav className="nav-bar indigo lighten-1">
         <div className="nav-wrapper">
           <a href="/" className="brand-logo">  Tap News</a>
           <ul id="nav-mobile"  className="right">
             {Auth.isUserAuthenticated() ?
               (<div>
                   <li>{Auth.getEmail()}</li>
                   <li><Link to="/logout">Log out</Link></li>
                </div>)
                :
                (<div>
                    <li><Link to="/login">Log in</Link></li>
                    <li><Link tp="/signup">Sign up</Link></li>
                </div>)
               }
            </ul>
        </div>
    </nav>
    <br/>
    {children}
 </div>
);

export default Base;