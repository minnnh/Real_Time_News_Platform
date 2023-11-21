import React, { useState, useEffect } from 'react';
import Auth from '../Auth/Auth';
import LoginForm from './LoginForm';
import { useNavigate } from 'react-router-dom';

const WEB_SERVER = 'http://localhost:3000';

const LoginPage = () => {
    const [state, setState] = useState({
        errors: {},
        user: {
            email: '',
            password: ''
        },
    });

    // const validUser = true;
    const navigate = useNavigate();

    const processForm = async (event) => {
        event.preventDefault();

        // Check if state.user is defined before attempting to destructure
        if (!state.user) {
            console.error('state.user is undefined');
            navigate('/login');
            return
            // const validUser = false;
            // catch(error);
        }

        const { email, password } = state.user;

        console.log('email:', email);
        console.log('password:', password);

        const url = WEB_SERVER + '/auth/login';
        const request = new Request(
            url,
            {
                method: 'Post',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );

        try {
            const response = await fetch(request);
            // status 200: OK status
            if (response.status === 200) {
                setState({
                    errors: {} 
                });

                const json = await response.json();
                console.log(json);
                Auth.authenticateUser(json.token, email);

                // Navigate after successful authentication
                navigate('/');
            } else {
                console.log('Login failed');
                const json = await response.json();
                const errors = json && json.errors ? json.errors : {};
                errors.message = json && json.message ? json.message : 'Unknown error';
                setState({ errors });
            }
        } catch (error) {
            console.error('Error during login:', error);
        }
    }

    const changeUser = (event) => {
        const field = event.target.name;
        const user = { ...state.user };
        user[field] = event.target.value;

        setState({
            ...state,
            user,
            errors: {}, // Initialize or clear errors when changing user data
        });

    }

    return (
        <LoginForm
            onSubmit={processForm}
            onChange={changeUser}
            errors={state.errors}
            user={state.user}
            // validUser = validUser
        />
    );
}

export default LoginPage;
