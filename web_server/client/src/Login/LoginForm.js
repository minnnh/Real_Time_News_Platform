import React, { useEffect } from 'react';
import './LoginForm.css';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';

const LoginForm = ({
    onSubmit,
    onChange,
    errors,
    user,
    // validUser = 'valid',
}) => ( 
    <div className="container">
        <div className="card-panel login-panel">

            <form className="col s12" action="/" onSubmit={onSubmit}>
                <h4 className="center-align">Login</h4>
                {(!user) && <div className="row"><p className="re-enter-message">! Please re-enter both of your email and password.</p></div>}
                {errors.message && <div className="row"><p className="error-message">{errors.message}</p></div>}
                <div className="row">
                <div className="input-field col s12">
                    <input className="validate" id="email" type="email" name="email" onChange={onChange}/>
                    <label htmlFor='email'>Email</label>
                </div>
                </div>
                {errors.email && <div className="row"><p className="error-message">{errors.email}</p></div>}
                <div className="row">
                <div className="input-field col s12">
                    <input className="validate" id="password" type="password" name="password" onChange={onChange}/>
                    <label htmlFor='password'>Password</label>
                </div>
                </div>
                {errors.password && <div className="row"><p className="error-message">{errors.password}</p></div>}
                <div className="row right-align">
                <input type="submit" className="waves-effect waves-light btn indigo lighten-1" value='Log in'/>
                </div>
                <div className="row">
                <p className="right-align"> New to Tap News?  <Link to="/signup">Sign Up</Link></p>
                </div>
            </form>  
        </div>
    </div>
);


LoginForm.propTypes = {
    onSubmit: PropTypes.func.isRequired,
    onChange: PropTypes.func.isRequired,
    errors: PropTypes.object.isRequired,
    user: PropTypes.object.isRequired
};

export default LoginForm;