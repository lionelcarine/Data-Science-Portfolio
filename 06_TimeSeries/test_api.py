from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_xgb():
    response = client.get("/predict/xgb")
    assert response.status_code == 200
    assert "forecast_xgb" in response.json()

def test_predict_prophet():
    response = client.get("/predict/prophet")
    assert response.status_code == 200
    assert "forecast_prophet" in response.json()

def test_predict_lstm():
    response = client.get("/predict/lstm")
    assert response.status_code == 200
    assert "forecast_lstm" in response.json()
