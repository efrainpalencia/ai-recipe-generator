# 1️⃣ Use Node.js for building the frontend
FROM node:18-alpine AS builder

# Set working directory inside container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the frontend
RUN npm run build

# 2️⃣ Use nginx for serving the built frontend
FROM nginx:alpine

# Set working directory
WORKDIR /usr/share/nginx/html

# Ignore tests during build
RUN rm -rf src/**/*.test.tsx

# Remove default nginx static assets
RUN rm -rf ./*

# Copy built frontend from previous step
COPY --from=builder /app/dist .

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port that Nginx will run on
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
