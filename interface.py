
import tkinter as tk


#PROPORÇÕES
largura = 1600
altura = 900


#FONTES
fonte_titulo = ("Inter",16,"bold")


#CORES
cor_fundo = ("#e4ebf1")
cor_branca = ("#FFFFFF")
cor_preto = ("#000000")
cor_fundo_botao = ("#050f44")


#TELAS
#tela 1 -inicial
#tela 2 -gerenciamento materias
#tela 3 -gerenciamento tarefas
#tela 4 -planejamento semanal
#tela 5 -estatisticas e histórico


def carregar_imagens():
    global imagem_tela_inicial
    global imagem_botao_inicio
    global imagem_botao_materias
    global imagem_botao_tarefas
    global imagem_botao_planejamento
    global imagem_botao_cronometro
    global imagem_botao_historico
    global imagem_botao_estatisticas
    global imagem_botao_sair


    imagem_botao_materias = tk.PhotoImage(file="imagens/botao_materias.png")
    imagem_tela_inicial = tk.PhotoImage(file="imagens/tela_inicial.png")
    imagem_botao_inicio = tk.PhotoImage(file="imagens/botao_inicio.png")
    imagem_botao_tarefas = tk.PhotoImage(file="imagens/botao_tarefas.png")
    imagem_botao_planejamento = tk.PhotoImage(file="imagens/botao_planejamento.png")
    imagem_botao_cronometro = tk.PhotoImage(file="imagens/botao_cronometro.png")
    imagem_botao_historico = tk.PhotoImage(file="imagens/botao_historico.png")
    imagem_botao_estatisticas = tk.PhotoImage(file="imagens/botao_estatisticas.png")
    imagem_botao_sair = tk.PhotoImage(file="imagens/botao_sair.png")

janela = None


def interface(tela,mudar_tela):
    if tela == 1:
        fundo = tk.Label(janela,bg=cor_fundo,image=imagem_tela_inicial)
        fundo.place(x=0,y=0)
        
        botao_inicio = tk.Button(janela,image=imagem_botao_inicio,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_inicio.place(relx = 0.1, rely = 0.15,anchor="center")

        botao_materias = tk.Button(janela,image=imagem_botao_materias,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_materias.place(relx = 0.1, rely = 0.22,anchor="center")

        botao_tarefas = tk.Button(janela,image=imagem_botao_tarefas,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_tarefas.place(relx = 0.1, rely = 0.29,anchor="center")

        botao_planejamento=tk.Button(janela,image=imagem_botao_planejamento,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_planejamento.place(relx = 0.1, rely = 0.36,anchor="center")

        botao_cronometro=tk.Button(janela,image=imagem_botao_cronometro,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_cronometro.place(relx = 0.1, rely = 0.43,anchor="center")

        botao_historico=tk.Button(janela,image=imagem_botao_historico,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_historico.place(relx = 0.1, rely = 0.50,anchor="center")

        botao_estatisticas=tk.Button(janela,image=imagem_botao_estatisticas,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_estatisticas.place(relx = 0.1, rely = 0.57,anchor="center")

        botao_sair=tk.Button(janela,image=imagem_botao_sair,relief="flat",highlightthickness=0,bg=cor_fundo_botao)
        botao_sair.place(relx = 0.1, rely = 0.9,anchor="center")

        