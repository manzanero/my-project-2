import json

import requests

start = "2025-02-26"
end = "2025-02-26"


with open('file.txt', 'r', encoding='utf8') as f:
    secret = f.read()


def get_neos(start_date, end_date):
    respuesta = requests.get("https://api.nasa.gov/neo/rest/v1/feed", params={
        "start_date": start_date,
        "end_date": end_date,
        "api_key": secret
    })

    return json.loads(respuesta.text)


print(get_neos(start, end))
