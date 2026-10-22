#Estatisticas.py: registrar, na aba de estatísticas, alguns dados do usuário, incluindo:
#Tempo total de estudo, tempo de estudo por matéria, por dia, total de sessões completas;

import historico
dados = historico.obter_historico()

def estatisticas():
    global tempo_total, tempo_materia

    tempo_total = 0
    tempo_materia = {}

    for sessao in dados:
        tempo_total += sessao["duracao"]


