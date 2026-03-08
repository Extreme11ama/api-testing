from utils.client_api import APIClient

client = APIClient()

def test_delete_post():
    response = client.deletePost(1)

    assert response.status_code == 200