from Factory import CPFouCNPJouCEP
from Datetime import MomentoDoCadastro
from CELULAR import Celular


cpf_do_usuario = '04972118237'
cnpj_do_usuario = '33592510000154'
celular_do_usuario = '5591985994001'
cep_do_usuario = '66083390'

teste = CPFouCNPJouCEP.factory(cpf_do_usuario)
print(teste)

teste2 = Celular(celular_do_usuario)
print(teste2)

teste3 = MomentoDoCadastro()
print(teste3)
print(teste3.retorna_tempo_de_cadastro())

teste4 = CPFouCNPJouCEP.factory(cep_do_usuario)
print(teste4)

bau = teste4.retornar_json()
for elemento in dict(bau).items():
    print(elemento)
