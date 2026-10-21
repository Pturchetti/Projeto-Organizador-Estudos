import json
import os

def carregar(nome):
    caminho = "dados/" + nome + ".json"
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return []

def salvar(nome, dados):
    os.makedirs("dados", exist_ok=True)
    with open("dados/" + nome + ".json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)