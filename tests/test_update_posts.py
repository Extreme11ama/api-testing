def test_update_post(client):
    updated = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }
    response = client.updatePost(1, updated)
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Updated Title"