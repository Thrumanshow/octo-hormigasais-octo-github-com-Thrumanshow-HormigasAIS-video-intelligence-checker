import requests

def test_api_responds_200():
    url = "http://localhost:8000"  # Cambia esta URL según la base de tu API
    response = requests.get(url)
    assert response.status_code == 200
