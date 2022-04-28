import validate_cpf


class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf
        self.validar()

    def validar(self):
        cpf_valido = validate_cpf.is_valid(self.cpf)
        if not cpf_valido:
            raise ValueError('CPF inválido')

    def formatacao(self):
        bloco_1 = self.cpf[:3]
        bloco_2 = self.cpf[3:6]
        bloco_3 = self.cpf[6:9]
        bloco_4 = self.cpf[9:]

        cpf_formatado = f'{bloco_1}.{bloco_2}.{bloco_3}-{bloco_4}'
        return cpf_formatado

    def __str__(self):
        return self.formatacao()
