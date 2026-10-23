def cadastrar_tarefa(tarefas, id_materia, titulo, descricao=""):
    titulo = titulo.strip()
    descricao = descricao.strip()

    if titulo == "":
        raise ValueError("O nome da tarefa é inválido!")
    
    if id_materia is None or str(id_materia).strip() == "":
        raise ValueError("O ID da Matéria é obrigatório!")
    try:
        id_materia = int(id_materia)
    except ValueError:
        raise ValueError("O ID da Matéria deve ser um número!")
    
    for tarefa in tarefas:
        if tarefa["titulo"].lower() == titulo.lower() and tarefa.get("id_materia") == id_materia:
            raise ValueError("Tarefa já cadastrada nesta matéria!")
            
    novo_id = 1
    for tarefa in tarefas:
        if tarefa["id"] >= novo_id:
            novo_id = tarefa["id"] + 1
            
    nova_tarefa = {
        "id": novo_id, 
        "id_materia": id_materia,
        "titulo": titulo, 
        "descricao": descricao, 
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas(tarefas):
    return sorted(tarefas, key=lambda tarefa: tarefa["titulo"].lower())

def buscar_tarefa(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None

def editar_tarefa(tarefas, id_tarefa, novo_titulo, nova_descricao=None):
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa is None:
        return None
        
    novo_titulo = novo_titulo.strip()
    if novo_titulo == "":
        raise ValueError("O nome da tarefa é inválido!")
        
    for outra_tarefa in tarefas:
        if outra_tarefa["id"] != id_tarefa and outra_tarefa["titulo"].lower() == novo_titulo.lower() and outra_tarefa.get("id_materia") == tarefa.get("id_materia"):
            raise ValueError("Tarefa já existente nesta matéria!")
            
    tarefa["titulo"] = novo_titulo
    if nova_descricao is not None:
        tarefa["descricao"] = nova_descricao.strip()
        
    return tarefa

def remover_tarefa(tarefas, id_tarefa):
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa is None:
        return False
    tarefas.remove(tarefa)
    return True

def concluir_tarefa(tarefas, id_tarefa):
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa is None:
        return False
    
    if tarefa.get("concluida"):
        raise ValueError("Tarefa já concluída!")
        
    tarefa["concluida"] = True
    return tarefa
