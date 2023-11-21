import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Base from './Base/Base';
import App from './App/App';
import LoginPage from './Login/LoginPage';
import SignUpPage from './SignUp/SignUpPage';
import Auth from './Auth/Auth';

const AppSelector = () => {
  const navigate = useNavigate();

  if (Auth.isUserAuthenticated()) {
    // return <App />;
    return <Base><App /></Base>;
  } else {
    navigate('/login'); // Redirect to login if not authenticated
    return <LoginPage />;
  }
};

const LoginHandler = () => {
  return <LoginPage />;
};

const SignUpHandler = () => {
  return <SignUpPage />;
};

const LogoutHandler = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const logout = async () => {
      try {
        await Auth.deAuthenticateUser();
        navigate('/', { replace: true });
      } catch (error) {
        console.error('Logout failed:', error);
      }
    };

    logout();
  }, [navigate]);

  return null;
};



export { AppSelector, LoginHandler, SignUpHandler, LogoutHandler };


