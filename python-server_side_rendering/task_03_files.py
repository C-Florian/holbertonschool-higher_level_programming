from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read data from a JSON file
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to read data from a CSV file and convert to list of dictionaries
def read_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return [
            {
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            }
            for row in reader
        ]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to display a list of items loaded from a JSON file
@app.route('/items')
def items():
    with open("items.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        items = data.get("items", [])
    return render_template("items.html", items=items)

# Route to display products from either a JSON or CSV file
@app.route('/products')
def display_products():
    source = request.args.get('source')  # Get the source type from query parameters
    product_id = request.args.get('id', type=int)  # Optional filter by product ID

    # Choose data source based on the query parameter
    if source == "json":
        try:
            products = read_json("products.json")
        except Exception as e:
            return render_template("product_display.html", error="Error reading JSON file.")
    elif source == "csv":
        try:
            products = read_csv("products.csv")
        except Exception as e:
            return render_template("product_display.html", error="Error reading CSV file.")
    else:
        return render_template("product_display.html", error="Wrong source")

    # If a product ID is specified, filter the list
    if product_id is not None:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=products)

# Run the Flask application only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)
