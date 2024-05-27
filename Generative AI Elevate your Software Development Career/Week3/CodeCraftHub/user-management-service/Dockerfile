# Use the official Node.js image as the base image
FROM node:20.13.1

# Create and change to the app directory
WORKDIR /app

# Copy the package.json and package-lock.json from the root to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code to the app directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
