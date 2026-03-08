from utils.client_api import APIClient

client = APIClient()

def test_getPost():
    response = client.getPost(1)

    assert response.status_code == 200



