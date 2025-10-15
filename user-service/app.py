# user-service/app.py
from flask import Flask, jsonify
app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route("/health")
def health():
    return jsonify({"status":"ok","service":"user-service"})

@app.route("/users")
def users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

