// src/models/userModel
// Import mongoose for MongoDB interaction
const mongoose = require('mongoose');

// Define user schema
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

// Create User model based on the schema
const User = mongoose.model('User', userSchema);

module.exports = User;
