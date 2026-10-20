#cadastro e organização das materias
def cadastrar_materia(materias, nome):
    nome = nome.strip()
    if nome == "":
        raise ValueError("Inválido!")
    for materia in materias:
        if materia["nome"].lower() == nome.lower():
            raise ValueError("Matéria já cadastrada!")
    novo_id = 1
    for materia in materias:
        if materia["id"] >= novo_id:
            novo_id = materia["id"] + 1
    nova_materia = {"id" : novo_id, "nome" : nome}
    materias.append(nova_materia)
    return nova_materia

def listar_materias(materias):
    return sorted(materias, key = lambda materia : materia["nome"].lower())

def buscar_materia(materias, id_materia):
    for materia in materias:
        if materia["id"] == id_materia:
            return materia
    return None

def editar_materia(materias, id_materia, novo_nome):
    nova_materia = buscar_materia(materias, id_materia)
    if nova_materia is None:
        return None
    novo_nome = novo_nome.strip()
    if novo_nome == "":
        raise ValueError("Inválido!")
    for materia in materias:
        if materia["id"] != id_materia and materia["nome"].lower() == novo_nome.lower():
            raise ValueError("Matéria já existente!")
    nova_materia["nome"] = novo_nome
    return nova_materia

def remover_materia(materias, id_materia):
    materia = buscar_materia(materias, id_materia)
    if materia is None:
        return False
    materias.remove(materia)
    return True