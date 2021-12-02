""" 
    Test file that contains test for all endpoints in our main.py file
"""

from fastapi.testclient import TestClient

from main import app
import crud

client = TestClient(app)

def test_create_transaction():
    """
        functions that test our create transaction endpoint 
        to make sure there are no errors each time we make changes
    """

    transaction = {
        "value": 123,
        "receiver": "foo bar",
        "sender": "bar foo",
    }
    response = client.post(
        "/transactions/",
        json={**transaction},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": response.json().timestamp,
        "value": 123,
        "receiver": "foo bar",
        "sender": "bar foo",
        "timestamp": response.json().timestamp,
        "confirmed": False
    }

def test_read_items():
    """
        functions that test our create transaction endpoint 
        to make sure there are no errors each time we make changes
    """

    response = client.get("/transactions")
    assert response.status_code == 200
    assert isinstance(response, list)


def test_read_item_with_id():
    """
        functions that test our create transaction endpoint 
        to make sure there are no errors each time we make changes
    """

    response = client.get("/transactions/")
    assert response.status_code == 200
    assert isinstance(response, list)
