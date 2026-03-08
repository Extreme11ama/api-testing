from utils.client_api import APIClient
import pytest

client = APIClient()

def test_getPost():
    response = client.getPost(1)
    assert response.status_code == 200

def test_get_post_data():
    response = client.getPost(1)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_get_all_posts():
    response = client.getAllPosts()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_invalid_post():
    response = client.getPost(999)

    assert response.status_code == 404

@pytest.mark.parametrize("postID", [1, 5, 10])
def test_multiple_posts(postID):
    response = client.getPost(postID)

    assert response.status_code == 200

def test_response_time():
    response = client.getAllPosts()

    assert response.elapsed.total_seconds() < 2

def test_post_schema():
    response = client.getPost(1)
    data = response.json()

    expected_fields = ["userId", "id", "title", "body"]

    for field in expected_fields:
        assert field in data

