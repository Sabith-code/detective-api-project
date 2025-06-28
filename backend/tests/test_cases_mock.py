from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app import app


def test_create_case_db_failure():
    with patch("backend.app.cases.insert_one") as mock_insert:
        mock_insert.side_effect = Exception("DB insert failed")

        client = app.test_client()
        res = client.post("/cases", json={"title": "FailTest", "description": "Should fail"})

        # Since our route doesn't catch exceptions, this will likely be a 500
        assert res.status_code == 500 or res.status_code == 400  # Acceptable depending on how you handle it
