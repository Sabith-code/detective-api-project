import mongomock
import pytest

@pytest.fixture
def mock_db():
    client = mongomock.MongoClient()
    db = client["detective"]
    yield db

def test_insert_case(mock_db):
    inserted = mock_db.cases.insert_one({"title": "Mocked", "description": "Insert"})
    found = mock_db.cases.find_one({"_id": inserted.inserted_id})
    assert found["title"] == "Mocked"

def test_mock_insert_and_read():
    db = mongomock.MongoClient().detective
    inserted = db.cases.insert_one({"title": "mock", "description": "desc"})
    found = db.cases.find_one({"_id": inserted.inserted_id})
    assert found["title"] == "mock"
