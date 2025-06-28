from flask import Flask, request, jsonify
from flask_cors import CORS
from bson import ObjectId
from bson.errors import InvalidId
from db import cases, clues, suspects

app = Flask(__name__)
CORS(app)

def to_json(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

def is_valid_objectid(id):
    try:
        ObjectId(id)
        return True
    except InvalidId:
        return False

@app.route("/cases", methods=["POST"])
def create_case():
    data = request.json
    title = data.get("title", "").strip()
    description = data.get("description", "").strip()

    if not title or not description:
        return jsonify({"error": "Title and description required"}), 400

    case = { "title": title, "description": description }
    result = cases.insert_one(case)
    case["id"] = str(result.inserted_id)
    return jsonify(case), 201

@app.route("/cases", methods=["GET"])
def get_cases():
    all_cases = list(cases.find())
    return jsonify([to_json(c) for c in all_cases]), 200

@app.route("/cases/<id>", methods=["DELETE"])
def delete_case(id):
    if not is_valid_objectid(id):
        return jsonify({"error": "Invalid case ID"}), 400
    cases.delete_one({"_id": ObjectId(id)})
    clues.delete_many({"case_id": id})
    suspects.delete_many({"case_id": id})
    return jsonify({"message": "Case deleted"}), 200

@app.route("/clues", methods=["POST"])
def create_clue():
    data = request.json
    case_id = data.get("case_id", "").strip()
    detail = data.get("detail", "").strip()

    if not case_id or not detail:
        return jsonify({"error": "Case ID and detail required"}), 400

    if not is_valid_objectid(case_id):
        return jsonify({"error": "Invalid case ID"}), 400

    result = clues.insert_one({ "case_id": case_id, "detail": detail })
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route("/clues/<case_id>", methods=["GET"])
def get_clues(case_id):
    if not is_valid_objectid(case_id):
        return jsonify({"error": "Invalid case ID"}), 400
    clue_list = list(clues.find({ "case_id": case_id }))
    return jsonify([to_json(c) for c in clue_list]), 200

@app.route("/suspects", methods=["POST"])
def create_suspect():
    data = request.json
    case_id = data.get("case_id", "").strip()
    name = data.get("name", "").strip()

    if not case_id or not name:
        return jsonify({"error": "Case ID and name required"}), 400

    if not is_valid_objectid(case_id):
        return jsonify({"error": "Invalid case ID"}), 400

    result = suspects.insert_one({ "case_id": case_id, "name": name })
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route("/suspects/<case_id>", methods=["GET"])
def get_suspects(case_id):
    if not is_valid_objectid(case_id):
        return jsonify({"error": "Invalid case ID"}), 400
    suspect_list = list(suspects.find({ "case_id": case_id }))
    return jsonify([to_json(s) for s in suspect_list]), 200

if __name__ == "__main__":
    app.run(debug=True)
