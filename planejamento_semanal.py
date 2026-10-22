import persistencia
from datetime import datetime, timedelta


planejamentos = persistencia.carregar("planejamentos") or []


def salvar():
    persistencia.salvar("planejamentos", planejamentos)


def buscar_planejamento(id_planejamento):
    for planejamento in planejamentos:
        if planejamento["id"] == id_planejamento:
            return planejamento
    return None


def listar_dia(data):
    lista = []

    for planejamento in planejamentos:
        if planejamento["data"] == data:
            lista.append(planejamento)

    lista.sort(key=lambda planejamento: planejamento["horario"])

    return lista


def listar_semana(data_inicio):
    semana = []

    for i in range(7):
        data = data_inicio + timedelta(days=i)

        semana.append({
            "data": data.strftime("%Y-%m-%d"),
            "planejamentos": listar_dia(
                data.strftime("%Y-%m-%d")
            )
        })

    return semana


def verificar_conflito(data, horario, duracao, id_atual=None):
    inicio = datetime.strptime(
        horario,
        "%H:%M"
    )

    fim = inicio + timedelta(
        minutes=duracao
    )

    for planejamento in planejamentos:

        if planejamento["data"] != data:
            continue

        if planejamento["id"] == id_atual:
            continue

        inicio_existente = datetime.strptime(
            planejamento["horario"],
            "%H:%M"
        )

        fim_existente = inicio_existente + timedelta(
            minutes=planejamento["duracao"]
        )

        if inicio < fim_existente and fim > inicio_existente:
            return True

    return False


def adicionar_planejamento(
    data,
    horario,
    duracao,
    materia_id,
    descricao=""
):
    if verificar_conflito(
        data,
        horario,
        duracao
    ):
        raise ValueError(
            "Existe outro planejamento nesse horário."
        )

    novo_id = 1

    for planejamento in planejamentos:
        if planejamento["id"] >= novo_id:
            novo_id = planejamento["id"] + 1

    novo_planejamento = {
        "id": novo_id,
        "data": data,
        "horario": horario,
        "duracao": duracao,
        "materia_id": materia_id,
        "descricao": descricao
    }

    planejamentos.append(
        novo_planejamento
    )

    salvar()

    return novo_planejamento


def editar_planejamento(
    id_planejamento,
    data,
    horario,
    duracao,
    materia_id,
    descricao=""
):
    planejamento = buscar_planejamento(
        id_planejamento
    )

    if planejamento is None:
        return None

    if verificar_conflito(
        data,
        horario,
        duracao,
        id_planejamento
    ):
        raise ValueError(
            "Existe outro planejamento nesse horário."
        )

    planejamento["data"] = data
    planejamento["horario"] = horario
    planejamento["duracao"] = duracao
    planejamento["materia_id"] = materia_id
    planejamento["descricao"] = descricao

    salvar()

    return planejamento


def remover_planejamento(id_planejamento):
    planejamento = buscar_planejamento(
        id_planejamento
    )

    if planejamento is None:
        return False

    planejamentos.remove(
        planejamento
    )

    salvar()

    return True