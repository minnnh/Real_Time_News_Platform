const jwt = require('jsonwebtoken');
const User = require('mongoose').model('User');
const PassportLocalStrategy = require('passport-local').Strategy;
const config = require('../config/config.json');

module.exports = new PassportLocalStrategy({
  usernameField: 'email',
  passwordField: 'password',
  session: false,
  passReqToCallback: true
}, async (req, email, password, done) => {
  const userData = {
    email: email.trim(),
    password: password
  };

  try {
    const user = await User.findOne({ email: userData.email }).exec();

    if (!user) {
      const error = new Error('Not a user. Incorrect email or password');
      error.name = 'IncorrectCredentialsError';
      return done(error);
    }

    const isMatch = await user.comparePassword(userData.password);

    if (!isMatch) {
      const error = new Error('Incorrect email or password');
      error.name = 'IncorrectCredentialsError';
      return done(error);
    }

    const payload = {
      sub: user._id
    };

    // create a token string
    const token = jwt.sign(payload, config.jwtSecret);
    const data = {
      name: user.email
    };

    return done(null, token, data);
  } catch (err) {
    return done(err);
  }
});
