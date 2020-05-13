from app import app

app.config['TESTING'] = True

with app.test_client() as client:
    def test_api():
        response = client.post(json={
            "text": "Der Text handelt in Velbert vom Bürgermeister Max Mustermann."
        })
        responseData = response.get_json()

        assert {"entities": [{"name": "Velbert", "label": "LOC", "startChar": 20, "endChar": 27}, {"name": "Max Mustermann", "label": "PER", "startChar": 46, "endChar": 60}]} == responseData
