import requests
import pytest
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"

post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_multiple_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=post_schema)

def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    validate(instance=response.json(), schema=post_schema)
