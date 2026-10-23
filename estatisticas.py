#Estatisticas.py: registrar, na aba de estatísticas, alguns dados do usuário, incluindo:
#Tempo total de estudo, por dia, total de dias estudados, tempo médio de estudo por dia

def estatisticas(dias_historico):
    dias_estudados = 0
    tempo_total = 0
    tempo_dia = {}
    tempo_medio = 0

    for dia in dias_historico:
        horas = dia.get("horas_estudadas", 0)

        if horas > 0:
            dias_estudados += 1
            tempo_total += horas
            tempo_dia[dia["data"]] = horas

    if dias_estudados > 0:
        tempo_medio = tempo_total / dias_estudados

    return tempo_total, tempo_dia, dias_estudados, tempo_medio
