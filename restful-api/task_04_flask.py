#!/usr/bin/env python3
"""
Task 04 - Simple Flask API with GET and POST endpoints
"""

from flask import Flask, jsonify, request

# Instantiate the Flask application
app = Flask(__name__)

# In-memory dictionary to store users (username -> user info)
users = {}

@app.route("/")
def home():
    """
    Root endpoint - returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Status endpoint - confirms the API is running.
    """
    return "OK"


@app.route("/data")
def list_usernames():
    """
    Returns a list of all usernames in the users dictionary.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Returns user data for a specific username.
    If the user doesn't exist, return an error.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles POST requests to add a new user.
    The request must include a 'username'.
    """
    data = request.get_json()

    # Validate input
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run()

