"""hacer get a esta url: https://api.chucknorris.io/jokes/random
si no aparece "Chuck Norris" en el "value" de la respuesta hacer un
raise AssertionError("Error")
"""
import json

import requests

respuesta = requests.get("https://api.chucknorris.io/jokes/random")

respuesta_diccionario = json.loads(respuesta.text)
value = respuesta_diccionario["value"]

if "Chuck Norrirrgers" not in value:
    raise AssertionError("Error")

print(value)