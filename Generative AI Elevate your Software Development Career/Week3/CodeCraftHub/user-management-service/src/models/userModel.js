// src/models/userModel.js
// Import mongoose for MongoDB interaction
const mongoose = require('mongoose');

/**
 * Defines the schema for user data.
 * @const {Schema} userSchema
 * @property {String} username - The username of the user. Required and must be unique.
 * @property {String} password - The password of the user. Required.
 */
const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
});

/**
 * Creates a User model based on the userSchema.
 * @const {Model} User
 */
const User = mongoose.model('User', userSchema);

module.exports = User;
