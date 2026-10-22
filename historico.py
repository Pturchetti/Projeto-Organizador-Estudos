from datetime import date, datetime

DIAS_SEMANA = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira",
               "sexta-feira", "sábado", "domingo"]

def obter_dia(historico, data = None):
    if data is None:
        data = date.today().isoformat()
    for dia in historico:
        if dia["data"] == data:
            return dia
    dia_semana = DIAS_SEMANA[datetime.strptime(data, "%Y-%m-%d").weekday()]
    dia = {"data" : data, "dia_semana" : dia_semana, "horas_estudadas" : 0, "tarefas_feitas" : [], "materias" : [], "sessoes_pomodoro" : 0}
    historico.append(dia)
    return dia

def registrar_estudo(historico, id_materia, duracao, data = None):
    dia = obter_dia(historico, data)
    dia["horas_estudadas"] += duracao
    if id_materia is None:
        return
    for item in dia["materias"]:
        if item["id_materia"] == id_materia:
            item["duracao"] += duracao
            return
    dia["materias"].append({"id_materia" : id_materia, "duracao" : duracao})

def registrar_sessao_pomodoro(historico, duracao_minutos, data = None):
    dia = obter_dia(historico, data)
    registrar_estudo(historico, None, duracao_minutos / 60, data)
    dia["sessoes_pomodoro"] = dia.get("sessoes_pomodoro", 0) + 1

def registrar_tarefa_concluida(historico, id_tarefa, data = None):
    dia = obter_dia(historico, data)
    if id_tarefa not in dia["tarefas_feitas"]:
        dia["tarefas_feitas"].append(id_tarefa)