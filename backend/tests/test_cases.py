def test_create_case(client):
    res = client.post("/cases", json={"title": "Edge Case", "description": "Testing"})
    assert res.status_code == 201
    assert "id" in res.json and res.json["message"] == "Case created"

def test_create_case_missing_title(client):
    res = client.post("/cases", json={"description": "No title"})
    assert res.status_code == 400

def test_create_case_empty_fields(client):
    res = client.post("/cases", json={"title": "", "description": ""})
    assert res.status_code == 400

def test_update_case_invalid_id(client):
    res = client.put("/cases/invalidid123", json={"title": "Test", "description": "Test"})
    assert res.status_code in [400, 404]

def test_update_case_empty_fields(client):
    case = client.post("/cases", json={"title": "ToUpdate", "description": "Edit Me"}).json
    cid = case["id"]
    res = client.put(f"/cases/{cid}", json={"title": "", "description": ""})
    assert res.status_code == 400

def test_delete_case_invalid_id(client):
    res = client.delete("/cases/123badid")
    assert res.status_code in [400, 404]

def test_get_all_cases(client):
    res = client.get("/cases")
    assert res.status_code == 200
    assert isinstance(res.json, list)
