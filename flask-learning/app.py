from flask import Flask, jsonify, request
from database import db    
from models import Product                  

app = Flask(__name__)                          

# here we bring "Flask" class into our python programm, so we can create a flask application
#when someone visits '/', Flask calls home() and sends "Learning flask" back to the browser.
# this creates our flask application and stores in 'app' variable.
# #127.0.0.1:5000 - it is the address where flask development server is running

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db" #Use a SQLite database called products.db.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #connects our SQLAlchemy object to the Flask application.



@app.route("/")
def home():
    return "Product API is running"



# products = [
#     {"id": 1, "name": "Laptop", "price": 50000},
#     {"id": 2, "name": "Phone", "price": 20000},
#     {"id": 3, "name": "Headphones", "price": 3000}
# ]


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()

    return jsonify([
        {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        for product in products
    ]) 


@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = db.session.get(Product, id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price
    })

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data.get("name") or not data["name"].strip():
        return jsonify({"message": "Name is required"}), 400

    if data.get("price") is None or data["price"] < 0:
        return jsonify({"message": "Price must be 0 or greater"}), 400

    product = Product(
        id=data["id"],
        name=data["name"],
        price=data["price"]
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price
    }), 201

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()

    product = db.session.get(Product, id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    # Update name only if provided
    if "name" in data:
        if not data["name"] or not data["name"].strip():
            return jsonify({"message": "Name cannot be empty"}), 400

        product.name = data["name"]

    # Update price only if provided
    if "price" in data:
        if data["price"] is None or data["price"] < 0:
            return jsonify({"message": "Price must be 0 or greater"}), 400

        product.price = data["price"]

    db.session.commit()

    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price
    })

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = db.session.get(Product, id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "message": "Product deleted successfully"
    })



with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug = True)
