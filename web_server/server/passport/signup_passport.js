const User = require('mongoose').model('User');
const PassportLocalStrategy = require('passport-local').Strategy;

module.exports = new PassportLocalStrategy({
  usernameField: 'email',
  passwordField: 'password',
  passReqToCallback: true
}, async (req, email, password, done) => {
  try {
    const userData = {
      email: email.trim(),
      password: password
    };

    const newUser = new User(userData);

    // Save the new user to the database
    await newUser.save();

    console.log('New user data:', newUser);

    // You can also perform asynchronous operations here before calling 'done'
    // For example, you might want to send a confirmation email or log additional information

    // Finally, call 'done' to indicate the completion of the strategy
    return done(null, newUser);
  } catch (error) {
    console.error('Error creating new user:', error);
    return done(error);
  }
});

