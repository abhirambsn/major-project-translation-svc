from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_healthz_check():
    response = client.get("/api/v1/translate/healthz")
    assert response.status_code == 200
    assert response.json() == {
        "status": 200,
        "message": "Healthy",
        "data": None
    }

def test_translate():
    with client.websocket_connect("/ws/v1/translate") as websocket:
        websocket.send_json({
            "text": "Hello, World!",
            "src_lang": "eng_Latn",
            "tgt_lang": "spa_Latn"
        })
        response = websocket.receive_json()
        assert response["status"] == 200
        assert response["message"] == "Translation successful"
        assert response["data"]["text"].lower() == "¡hola, mundo!"
        assert isinstance(response["data"]["time"], float)