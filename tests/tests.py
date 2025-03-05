import unittest

import requests


class MyTestCase(unittest.TestCase):

    def test_sumar(self):
        respuesta = requests.get("http://localhost/calculadora/1/sumar/2")
        if not respuesta.text == "3":
            raise AssertionError("resultado invalido")

if __name__ == '__main__':
    unittest.main()
