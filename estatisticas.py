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
        horas = dia.get("horas_estudadas", 0)

        if horas > 0:
            dias_estudados += 1
            tempo_total += horas
            tempo_dia[dia["data"]] = horas

        for item in dia.get("materias", []):
            materia = item["id_materia"]
            tempo_materia[materia] = tempo_materia.get(materia, 0) + item["duracao"]

    materia_mais_estudada = None
    if tempo_materia:
        materia_mais_estudada = max(tempo_materia, key = tempo_materia.get)

    if dias_estudados > 0:
        tempo_medio = tempo_total / dias_estudados

    return tempo_total, tempo_dia, tempo_materia, dias_estudados, materia_mais_estudada, tempo_medio