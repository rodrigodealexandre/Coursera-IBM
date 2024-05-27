// src/routes/userRoutes.js
// Import required modules
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

// Define routes for user registration, login, and profile management
router.post('/register', userController.registerUser);
router.post('/login', userController.loginUser);
router.put('/:username', userController.updateUserProfile);

module.exports = router;
