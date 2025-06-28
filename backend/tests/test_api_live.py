import requests

BASE = "http://localhost:5000"

def test_api_get_cases():
    res = requests.get(f"{BASE}/cases")
    assert res.status_code == 200

def test_api_post_invalid_case():
    res = requests.post(f"{BASE}/cases", json={"title": ""})
    assert res.status_code in [400, 422]
