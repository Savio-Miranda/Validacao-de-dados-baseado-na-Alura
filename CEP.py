import re
import requests
import json


class Cep:
    def __init__(self, cep):
        self.cep = cep
        self.padrao = re.compile(r'(\d{2})(\d{3})(\d{3})')
        self.buscar_no_cep = re.search(self.padrao, self.cep)
        self.validar()

    def validar(self):
        if len(self.cep) != 8:
            raise ValueError('CEP deve conter 8 caracteres')

    def retornar_json(self):
        link = api + self.cep + '/json/'
        response = requests.get(link)
        dados = json.loads(response.text)
        return dados

    def __str__(self):
        bloco_1 = self.buscar_no_cep.group(1)
        bloco_2 = self.buscar_no_cep.group(2)
        bloco_3 = self.buscar_no_cep.group(3)
        return f'{bloco_1}.{bloco_2}-{bloco_3}'


api = r'http://www.viacep.com.br/ws/'
