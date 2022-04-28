from CPF import Cpf
from CNPJ import Cnpj
from CEP import Cep


class CPFouCNPJouCEP:
    @staticmethod
    def factory(documento):
        if len(documento) == 11:
            return Cpf(documento)

        elif len(documento) == 14:
            return Cnpj(documento)

        elif len(documento) == 8:
            return Cep(documento)

        raise ValueError('Entrada inválida')
