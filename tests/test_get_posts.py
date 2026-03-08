from utils.client_api import APIClient
import pytest


def test_getPost(client):
    response = client.getPost(1)
    assert response.status_code == 200

def test_get_post_data(client):
    response = client.getPost(1)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_get_all_posts(client):
    response = client.getAllPosts()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_invalid_post(client):
    response = client.getPost(999)

    assert response.status_code == 404

@pytest.mark.parametrize("postID", [1, 5, 10])
def test_multiple_posts(client, postID):
    response = client.getPost(postID)

    assert response.status_code == 200

def test_response_time(client):
    response = client.getAllPosts()

    assert response.elapsed.total_seconds() < 2

def test_post_schema(client):
    response = client.getPost(1)
    data = response.json()

    expected_fields = ["userId", "id", "title", "body"]

    for field in expected_fields:
        assert field in data

