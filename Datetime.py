from datetime import datetime, timedelta


class MomentoDoCadastro:
    def __init__(self):
        self.momento_do_cadastro = datetime.today()
        self.meses_do_ano = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

        self.dias_da_semana = ('segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira',
                               'sexta-feira', 'sábado', 'domingo')

    def retorna_mes(self):
        mes = self.momento_do_cadastro.month
        return self.meses_do_ano[mes]

    def retorna_dia_da_semana(self):
        dia_da_semana = self.momento_do_cadastro.weekday()
        return self.dias_da_semana[dia_da_semana]

    def retorna_tempo_de_cadastro(self):
        tempo_de_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_do_cadastro
        return tempo_de_cadastro

    def data_formatada(self):
        ano = self.momento_do_cadastro.year
        mes = self.retorna_mes()
        dia = self.momento_do_cadastro.day
        dia_da_semana = self.retorna_dia_da_semana()
        horario = self.momento_do_cadastro.strftime('%H:%M')

        return f'{dia_da_semana.capitalize()}, {dia} de {mes} de {ano}, às {horario}'

    def __str__(self):
        return self.data_formatada()
