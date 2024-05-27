// src/controllers/userController.js
const { registerUser, loginUser, getUserProfile } = require('../services/userService');

const register = async (req, res) => {
  try {
    const user = await registerUser(req.body);
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

const login = async (req, res) => {
  try {
    const { email, password } = req.body;
    const { user, token } = await loginUser(email, password);
    res.status(200).json({ user, token });
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

const profile = async (req, res) => {
  try {
    const userId = req.user.id;
    const user = await getUserProfile(userId);
    res.status(200).json(user);
  } catch (error) {
    res.status(404).json({ message: error.message });
  }
};

module.exports = { register, login, profile };
