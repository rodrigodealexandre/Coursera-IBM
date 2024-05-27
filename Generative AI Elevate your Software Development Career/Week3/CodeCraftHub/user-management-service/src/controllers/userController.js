// src/controllers/userController.js
const userService = require('../services/userService');

/**
 * Register a new user.
 * Hashes the password before saving to the database.
 * @async
 * @function registerUser
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 */
exports.registerUser = async (req, res) => {
  try {
    const newUser = await userService.registerUser(req.body);
    return res.status(201).json({ message: 'User registered successfully', user: newUser });
  } catch (error) {
    if (error.message === 'Username already exists') {
      return res.status(409).json({ message: error.message });
    }
    console.error('Registration error:', error);
    return res.status(500).json({ message: 'Internal server error' });
  }
};

/**
 * Login an existing user.
 * Validates the username and password, then generates a JWT token.
 * @async
 * @function loginUser
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 */
exports.loginUser = async (req, res) => {
  try {
    const { username, password } = req.body;
    const { user, token } = await userService.loginUser(username, password);
    return res.status(200).json({ token });
  } catch (error) {
    console.error('Login error:', error);
    return res.status(401).json({ message: error.message });
  }
};

/**
 * Update the user's profile.
 * Changes the username based on the provided new username.
 * @async
 * @function updateUserProfile
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 */
exports.updateUserProfile = async (req, res) => {
  try {
    const { username } = req.params;
    const { newUsername } = req.body;
    const updatedUser = await userService.updateUserProfile(username, newUsername);
    return res.status(200).json({ message: 'User profile updated successfully', user: updatedUser });
  } catch (error) {
    console.error('Profile update error:', error);
    return res.status(500).json({ message: 'Internal server error' });
  }
};
