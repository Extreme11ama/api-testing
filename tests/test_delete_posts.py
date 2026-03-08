def test_delete_post(client):
    response = client.deletePost(1)

    assert response.status_code == 200