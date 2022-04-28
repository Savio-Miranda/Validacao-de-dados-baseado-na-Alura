import re


class Celular:
    def __init__(self, telefone):
        self.telefone = telefone
        self.padrao = re.compile(r'(\d{2})(\d{2})(\d{4,5})(\d{4})')
        self.codigos_de_area = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24',
                                '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43',
                                '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62',
                                '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77',
                                '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92',
                                '93', '94', '95', '96', '97', '98', '99']
        self.buscar_no_telefone = re.search(self.padrao, self.telefone)
        self.validar()

    def validar(self):
        padrao_nove_digitos = len(self.telefone) != 13
        padrao_oito_digitos = len(self.telefone) != 12
        if padrao_nove_digitos and padrao_oito_digitos:
            raise ValueError('Telefone Inválido. Formato aceito: DDI + DDD + 9 a 8 dígitos')

        ddi = self.buscar_no_telefone.group(1)
        ddd = self.buscar_no_telefone.group(2)
        
        if ddi != '55':
            raise ValueError('DDI Inválido')

        elif ddd not in self.codigos_de_area:
            raise ValueError('DDD Inválido')

    def formatacao(self):
        ddi = self.buscar_no_telefone.group(1)
        ddd = self.buscar_no_telefone.group(2)
        bloco_1 = self.buscar_no_telefone.group(3)
        bloco_2 = self.buscar_no_telefone.group(4)
        return f'{ddi}+ ({ddd}) {bloco_1}-{bloco_2}'

    def __str__(self):
        return self.formatacao()
