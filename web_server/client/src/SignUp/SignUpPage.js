import React, { useState } from 'react';
import SignUpForm from './SignUpForm';
import { useNavigate } from 'react-router-dom';

const WEB_SERVER = 'http://localhost:3000'

const SignUpPage = () => {
  const [state, setState] = useState({
    errors: {},
    user: {
      email: '',
      password: '',
      confirm_password: '',
    },
  });

  const navigate = useNavigate();

  const processForm = async (event) => {
    event.preventDefault();

    // Check if state.user is defined before attempting to destructure
    if (!state.user) {
        console.error('state.user is undefined');
        navigate('/signup');
        return
        // const validUser = false;
        // catch(error);
    }

    const { email, password, confirm_password } = state.user;

    console.log('email:', email);
    console.log('password:', password);
    console.log('confirm_password:', confirm_password);

    if (password !== confirm_password) {
      return;
    }

    // Post signup data.
    const url = WEB_SERVER + '/auth/signup';
    const request = new Request(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: state.user.email,
        password: state.user.password,
      }),
    });

    fetch(request).then((response) => {
      if (response.status === 200) {
        setState({
          errors: {},
        });

        // Redirect to login page
        navigate('/login');
      } else {
        response.json().then((json) => {
          console.log(json);
          const errors = json.errors ? json.errors : {};
          errors.message = json.message;
          setState({ errors });
        });
      }
    });
  };

  const changeUser = (event) => {
    const field = event.target.name;
    const user = { ...state.user };
    user[field] = event.target.value;

    setState({
      ...state,
      user,
      errors: {
        ...state.errors,
        password: user.password !== user.confirm_password ? "Password and confirm password don't match" : '',
      },
    });
  };

  return (
    <SignUpForm
      onSubmit={(e) => processForm(e)}
      onChange={(e) => changeUser(e)}
      errors={state.errors}
      user={state.user}
    />
  );
};

export default SignUpPage;
