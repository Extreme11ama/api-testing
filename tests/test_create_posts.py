def test_create_post(client):
    exampleJSON = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    response = client.createPost(exampleJSON)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "Test Title"

def test_create_post_missing_fields(client):
    exampleJSON = {
        "title": "Missing body"
    }
    response = client.createPost(exampleJSON)

    assert response.status_code in [200, 201]