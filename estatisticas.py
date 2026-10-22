#Estatisticas.py: registrar, na aba de estatísticas, alguns dados do usuário, incluindo:
#Tempo total de estudo, tempo de estudo por matéria, por dia, total de dias estudados;
#Tempo médio de estudo por dia, matéria que o usuário mais estudou

def estatisticas(dias_historico):
    dias_estudados = 0
    tempo_total = 0
    tempo_materia = {}
    tempo_dia = {}
    tempo_medio = 0

    for dia in dias_historico:
        if dia["horas_estudadas"] > 0:
            dias_estudados += 1

        for item in dia["materias"]:
            materia = item["id_materia"]
            duracao = item["duracao"]
            data = dia["data"]

            if materia not in tempo_materia:
                tempo_materia[materia] = 0
            if data not in tempo_dia:
                tempo_dia[data] = 0

            tempo_total += duracao;
            tempo_materia[materia] += duracao
            tempo_dia[data] += duracao

    maior_tempo = 0
    materia_mais_estudada = None
        
    for materia, tempo in tempo_materia.items():
        if tempo > maior_tempo:
            maior_tempo = tempo
            materia_mais_estudada = materia

    if dias_estudados > 0:
        tempo_medio = tempo_total / dias_estudados

    return tempo_total, tempo_dia, tempo_materia, dias_estudados, materia_mais_estudada, tempo_medio
