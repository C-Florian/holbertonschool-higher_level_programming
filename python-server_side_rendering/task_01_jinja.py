from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page template

# Define the route for the "About" page
@app.route('/about')
def about():
    return render_template('about.html')  # Render the about page template

# Define the route for the "Contact" page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Render the contact page template

# Start the development server when this file is run directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the app with debug mode on port 5000
