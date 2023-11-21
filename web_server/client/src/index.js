import React from 'react';
import ReactDOM from 'react-dom';
import { createMemoryHistory } from 'history';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';  // Updated import statement
import { AppSelector, LoginHandler, SignUpHandler, LogoutHandler } from './routes';

const history = createMemoryHistory();


const Root = () => {
  // const navigate = useNavigate();
  return (
    <Router history={history}>
      <Routes>
        <Route path="/" element={<AppSelector />} />
        <Route path="/login" element={<LoginHandler />} />
        <Route path="/signup" element={<SignUpHandler />} />
        <Route path="/logout" element={<LogoutHandler />} />
      </Routes>
    </Router>
  );
};

ReactDOM.render(<Root />, document.getElementById('root'));
