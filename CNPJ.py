import validate_cnpj


class Cnpj:
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.validar()

    def validar(self):
        cnpj_valido = validate_cnpj.is_valid(self.cnpj)
        if not cnpj_valido:
            raise ValueError('CNPJ inválido')

    def formatacao(self):
        bloco_1 = self.cnpj[:2]
        bloco_2 = self.cnpj[2:5]
        bloco_3 = self.cnpj[5:8]
        bloco_4 = self.cnpj[8:12]
        bloco_5 = self.cnpj[12:]

        cnpj_formatado = f'{bloco_1}.{bloco_2}.{bloco_3}/{bloco_4}-{bloco_5}'
        return cnpj_formatado

    def __str__(self):
        return self.formatacao()
