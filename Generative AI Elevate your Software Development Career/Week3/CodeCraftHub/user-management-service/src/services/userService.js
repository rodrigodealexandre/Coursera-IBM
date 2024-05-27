// src/controllers/userService.js
const User = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

dotenv.config();

/**
 * Register a new user.
 * Hashes the password before saving to the database.
 * @async
 * @function registerUser
 * @param {Object} userData - The user data object.
 * @returns {Object} newUser - The newly created user object.
 * @throws Will throw an error if the username already exists.
 */
const registerUser = async (userData) => {
  const { username, password } = userData;

  try {
    const existingUser = await User.findOne({ username });
    if (existingUser) {
      throw new Error('Username already exists');
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();

    return newUser;
  } catch (error) {
    console.error('Error during user registration:', error);
    throw error;
  }
};

/**
 * Login an existing user.
 * Validates the username and password, then generates a JWT token.
 * @async
 * @function loginUser
 * @param {String} username - The username of the user.
 * @param {String} password - The password of the user.
 * @returns {Object} - An object containing the user and the JWT token.
 * @throws Will throw an error if the username or password is invalid.
 */
const loginUser = async (username, password) => {
  try {
    const user = await User.findOne({ username });
    if (!user) {
      throw new Error('Invalid username or password');
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      throw new Error('Invalid username or password');
    }

    const token = jwt.sign({ username: user.username }, process.env.JWT_SECRET, {
      expiresIn: '1h',
    });

    return { user, token };
  } catch (error) {
    console.error('Error during user login:', error);
    throw error;
  }
};

/**
 * Update the user's profile.
 * Changes the username based on the provided new username.
 * @async
 * @function updateUserProfile
 * @param {String} username - The current username of the user.
 * @param {String} newUsername - The new username to be set.
 * @returns {Object} updatedUser - The updated user object.
 * @throws Will throw an error if the user is not found.
 */
const updateUserProfile = async (username, newUsername) => {
  try {
    const user = await User.findOneAndUpdate({ username }, { username: newUsername }, { new: true });
    if (!user) {
      throw new Error('User not found');
    }
    return user;
  } catch (error) {
    console.error('Error during profile update:', error);
    throw error;
  }
};

module.exports = { registerUser, loginUser, updateUserProfile };
