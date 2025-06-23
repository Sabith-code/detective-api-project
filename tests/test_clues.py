def test_add_clue(client):
    cid = client.post("/cases", json={"title": "ClueCase", "description": "clues!"}).json["id"]
    res = client.post("/clues", json={"case_id": cid, "detail": "A bloody hammer"})
    assert res.status_code == 201
    assert "id" in res.json and res.json["message"] == "Clue added"

def test_add_clue_missing_detail(client):
    cid = client.post("/cases", json={"title": "Clueless", "description": "?"}).json["id"]
    res = client.post("/clues", json={"case_id": cid})
    assert res.status_code == 400

def test_add_clue_invalid_case(client):
    res = client.post("/clues", json={"case_id": "badid", "detail": "Mismatch"})
    assert res.status_code in [400, 404]

def test_get_clues_invalid_case(client):
    res = client.get("/clues/invalid123")
    assert res.status_code in [400, 404]
