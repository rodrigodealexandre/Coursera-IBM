// src/routes/userRoutes.js
// Import the express module
const express = require('express');

// Create a new router object
const router = express.Router();

// Import the user controller
const userController = require('../controllers/userController');

// Define the route for user registration
// Calls the registerUser function in the user controller
router.post('/register', userController.registerUser);

// Define the route for user login
// Calls the loginUser function in the user controller
router.post('/login', userController.loginUser);

// Define the route for updating user profile
// Calls the updateUserProfile function in the user controller
// Expects the username to be provided as a URL parameter
router.put('/:username', userController.updateUserProfile);

// Export the router object to be used in other parts of the application
module.exports = router;
