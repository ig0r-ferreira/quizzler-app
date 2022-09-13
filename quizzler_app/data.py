import requests
import html

API_URL = "https://opentdb.com/api.php"
PARAMS = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(API_URL, params=PARAMS)
response.raise_for_status()
data = response.json()
question_data = data.get("results", [])

for record in question_data:
    record["question"] = html.unescape(record["question"])
