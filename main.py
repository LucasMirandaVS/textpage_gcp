
from flask import Flask, request, jsonify
from services.firestore import save_lead

app = Flask(__name__)

@app.route("/api/lead", methods=["POST"])
def handle_lead():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400

    try:
        save_lead(data["name"], data["email"])
        return jsonify({"message": "Lead saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
