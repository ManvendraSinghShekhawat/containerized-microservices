# product-service/app.py
from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Widget"},
    {"id": 2, "name": "Gadget"}
]

@app.route("/products/health")
def health():
    return jsonify({"status":"ok","service":"product-service"})

@app.route("/products")
def products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

