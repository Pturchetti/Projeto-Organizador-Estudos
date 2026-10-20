#cadastro e organização das materias
def cadastrar_materia(materias, nome, descricao = ""):
    nome = nome.strip()
    descricao = descricao.strip()

    if nome == "":
        raise ValueError("Inválido!")
    for materia in materias:
        if materia["nome"].lower() == nome.lower():
            raise ValueError("Matéria já cadastrada!")
    novo_id = 1
    for materia in materias:
        if materia["id"] >= novo_id:
            novo_id = materia["id"] + 1
    nova_materia = {"id" : novo_id, "nome" : nome, "descricao:" : descricao}
    materias.append(nova_materia)
    return nova_materia

def listar_materias(materias):
    return sorted(materias, key = lambda materia : materia["nome"].lower())

def buscar_materia(materias, id_materia):
    for materia in materias:
        if materia["id"] == id_materia:
            return materia
    return None

def editar_materia(materias, id_materia, novo_nome, nova_descricao = None):
    materia = buscar_materia(materias, id_materia)
    if materia is None:
        return None
    novo_nome = novo_nome.strip()
    if novo_nome == "":
        raise ValueError("Inválido!")
    for outra_materia in materias:
        if outra_materia["id"] != id_materia and materia["nome"].lower() == novo_nome.lower():
            raise ValueError("Matéria já existente!")
    materia["nome"] = novo_nome
    if nova_descricao is not None:
        materia["descricao"] = nova_descricao.strip()
    elif "descricao" not in materia:
        materia["descricao"] = ""
    return materia

def remover_materia(materias, id_materia):
    materia = buscar_materia(materias, id_materia)
    if materia is None:
        return False
    materias.remove(materia)
    return True