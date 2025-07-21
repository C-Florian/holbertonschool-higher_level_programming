import json
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page template

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')  # Render the about page template

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Render the contact page template

# Route to display items from a JSON file
@app.route('/items')
def items():
    # Open and read the JSON file with UTF-8 encoding
    with open("items.json", "r", encoding="utf-8") as f:
        data = json.load(f)  # Load JSON data into a Python dictionary
        items = data.get("items", [])  # Extract the list of items or return an empty list if missing

    # Render the items.html template with the items data passed as a variable
    return render_template("items.html", items=items)

# Run the app only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Launch the Flask server with debug mode on port 5000
