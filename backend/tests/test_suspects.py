def test_add_suspect(client):
    cid = client.post("/cases", json={"title": "SusCase", "description": "sus"}).json["id"]
    res = client.post("/suspects", json={"case_id": cid, "name": "Bob Smith"})
    assert res.status_code == 201
    assert "id" in res.json and res.json["message"] == "Suspect added"

def test_add_suspect_missing_name(client):
    cid = client.post("/cases", json={"title": "Sus2", "description": "??"}).json["id"]
    res = client.post("/suspects", json={"case_id": cid})
    assert res.status_code == 400

def test_add_suspect_invalid_case(client):
    res = client.post("/suspects", json={"case_id": "wrongid", "name": "Ghost"})
    assert res.status_code in [400, 404]

def test_get_suspects_invalid_case(client):
    res = client.get("/suspects/badid")
    assert res.status_code in [400, 404]
