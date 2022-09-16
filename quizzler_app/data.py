import requests

API_URL: str = "https://opentdb.com/api.php"
PARAMS: dict[str, int | str] = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(API_URL, params=PARAMS)
response.raise_for_status()
data = response.json()
question_data = data["results"]
