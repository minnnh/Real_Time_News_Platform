const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const UserSchema = new mongoose.Schema({
    email:{
        type: String,
        index: { unique: true }
    },
    password: String
});

// UserSchema.methods.comparePassword = function comparePassword(password, callback) {
//     bcrypt.compare(password, this.password, callback);
// };
UserSchema.methods.comparePassword = function comparePassword(password) {
    return new Promise((resolve, reject) => {
        bcrypt.compare(password, this.password, (err, isMatch) => {
            if (err) {
                return reject(err);
            }
            resolve(isMatch);
        });
    });
};

UserSchema.pre('save', function saveHook(next) {
    const user = this;

    //proceed furtherrr only if the password is modified or the user is new.
    if(!user.isModified('password')) return next();

    return bcrypt.genSalt((saltError, salt) => {
        if (saltError) { return next(saltError); }

        return bcrypt.hash(user.password, salt, (hashError, hash) => {
            if (hashError) { return next(hashError); }

            //replace a passward string with hashed value.
            user.password = hash;

            return next();
        });
    });
});

module.exports = mongoose.model('User', UserSchema);