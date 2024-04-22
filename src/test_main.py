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

def test_translate_word():
    with client.websocket_connect("/ws/v1/translate") as websocket:
        websocket.send_json({
            "text": "Hello",
            "src_lang": "eng_Latn",
            "tgt_lang": "spa_Latn"
        })
        response = websocket.receive_json()
        assert response["status"] == 200
        assert response["message"] == "Translation successful"
        assert response["data"]["text"].lower() == "hola. ¿ qué pasa?"
        assert isinstance(response["data"]["time"], float)
    
def test_translate_sentence():
    with client.websocket_connect("/ws/v1/translate") as websocket:
        websocket.send_json({
            "text": "Hello, how are you?",
            "src_lang": "eng_Latn",
            "tgt_lang": "spa_Latn"
        })
        response = websocket.receive_json()
        assert response["status"] == 200
        assert response["message"] == "Translation successful"
        assert response["data"]["text"].lower() == "hola, ¿cómo estás?"
        assert isinstance(response["data"]["time"], float)

def test_translate_paragraph():
    with client.websocket_connect("/ws/v1/translate") as websocket:
        websocket.send_json({
            "text": "The lush greenery of the forest enveloped us as we ventured deeper into its heart. The sunlight filtered through the dense canopy, casting playful shadows on the forest floor. Birds chirped melodiously, adding to the symphony of nature's song. With each step, the earth seemed to breathe beneath our feet, connecting us to the ancient rhythms of the wilderness.",
            "src_lang": "eng_Latn",
            "tgt_lang": "spa_Latn"
        })
        response = websocket.receive_json()
        assert response["status"] == 200
        assert response["message"] == "Translation successful"
        assert response["data"]["text"].lower() == "la exuberante verdura del bosque nos envolvió mientras nos aventurábamos más profundamente en su corazón. la luz del sol se filtró a través del denso dosel, lanzando sombras lúdicas en el suelo del bosque. los pájaros chirrieron melodiosamente, añadiendo a la sinfonía del canto de la naturaleza."
        assert isinstance(response["data"]["time"], float)