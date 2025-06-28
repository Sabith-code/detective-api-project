from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["detective_db"]
cases = db["cases"]
clues = db["clues"]
suspects = db["suspects"]

# Utility to convert ObjectId to string
def to_json(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

# ----------- CASE ROUTES -----------

@app.route("/cases", methods=["GET"])
def get_cases():
    all_cases = list(cases.find())
    return jsonify([to_json(c) for c in all_cases])

@app.route("/cases", methods=["POST"])
def add_case():
    data = request.get_json()
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()

    if not title or not description:
        return jsonify({"error": "Title and description are required."}), 400

    result = cases.insert_one({"title": title, "description": description})
    new_case = cases.find_one({"_id": result.inserted_id})
    return jsonify(to_json(new_case)), 201

@app.route("/cases/<case_id>", methods=["DELETE"])
def delete_case(case_id):
    cases.delete_one({"_id": ObjectId(case_id)})
    clues.delete_many({"case_id": case_id})
    suspects.delete_many({"case_id": case_id})
    return jsonify({"message": "Case deleted"}), 200

# ----------- CLUE ROUTES -----------

@app.route("/clues/<case_id>", methods=["GET"])
def get_clues(case_id):
    clue_list = list(clues.find({"case_id": case_id}))
    return jsonify([to_json(c) for c in clue_list])

@app.route("/clues", methods=["POST"])
def add_clue():
    data = request.get_json()
    case_id = data.get("case_id")
    detail = data.get("detail", "").strip()

    if not case_id or not detail:
        return jsonify({"error": "Case ID and clue detail are required."}), 400

    result = clues.insert_one({"case_id": case_id, "detail": detail})
    return jsonify(to_json(clues.find_one({"_id": result.inserted_id}))), 201

# ----------- SUSPECT ROUTES -----------

@app.route("/suspects/<case_id>", methods=["GET"])
def get_suspects(case_id):
    suspect_list = list(suspects.find({"case_id": case_id}))
    return jsonify([to_json(s) for s in suspect_list])

@app.route("/suspects", methods=["POST"])
def add_suspect():
    data = request.get_json()
    case_id = data.get("case_id")
    name = data.get("name", "").strip()

    if not case_id or not name:
        return jsonify({"error": "Case ID and suspect name are required."}), 400

    result = suspects.insert_one({"case_id": case_id, "name": name})
    return jsonify(to_json(suspects.find_one({"_id": result.inserted_id}))), 201

# ----------- MAIN -----------

if __name__ == "__main__":
    app.run(debug=True)
