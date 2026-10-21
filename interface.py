
import tkinter as tk
from tkinter import messagebox
import gerenciamento_materias

#PROPORÇÕES
largura = 1600
altura = 900


#FONTES
fonte_titulo = ("Inter",18,"bold")
fonte_palavras = ("Inter",12,"bold")

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
#tela 5 -cronometro
#tela 6 -histórico
#tela 7 -estatísticas


janela = None
resto_tela = None
nome_materia = None
id_materia = None
print_detalhes_materia = None

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
    global imagem_fundo
    global imagem_menu_lateral
    global imagem_balao_tarefas
    global imagem_botao_pause
    global imagem_botao_reload
    global imagem_botao_pomodoro
    global imagem_tela_cronometro
    global imagem_tela_materias
    global imagem_botao_cadastro_materias
    global imagem_tela_cadastro_materia
    global imagem_botao_confirmar

    imagem_botao_confirmar = tk.PhotoImage(file="imagens/botao_confirmar.png")
    imagem_tela_cadastro_materia = tk.PhotoImage(file="imagens/tela_cadastro_materia.png")
    imagem_tela_materias = tk.PhotoImage(file="imagens/tela_materias.png")
    imagem_botao_cadastro_materias = tk.PhotoImage(file="imagens/botao_cadastrar_materia.png")
    imagem_tela_cronometro = tk.PhotoImage(file="imagens/tela_cronometro.png")
    imagem_botao_pomodoro = tk.PhotoImage(file="imagens/botao_pomodoro.png")
    imagem_botao_reload = tk.PhotoImage(file="imagens/botao_reload.png")
    imagem_botao_pause = tk.PhotoImage(file="imagens/botao_pause.png")
    imagem_balao_tarefas = tk.PhotoImage(file="imagens/botao_tarefas.png")
    imagem_menu_lateral = tk.PhotoImage(file="imagens/menu_lateral.png")
    imagem_fundo = tk.PhotoImage(file="imagens/background.png")
    imagem_botao_materias = tk.PhotoImage(file="imagens/botao_materias.png")
    imagem_tela_inicial = tk.PhotoImage(file="imagens/tela_inicial.png")
    imagem_botao_inicio = tk.PhotoImage(file="imagens/botao_inicio.png")
    imagem_botao_tarefas = tk.PhotoImage(file="imagens/botao_tarefas.png")
    imagem_botao_planejamento = tk.PhotoImage(file="imagens/botao_planejamento.png")
    imagem_botao_cronometro = tk.PhotoImage(file="imagens/botao_cronometro.png")
    imagem_botao_historico = tk.PhotoImage(file="imagens/botao_historico.png")
    imagem_botao_estatisticas = tk.PhotoImage(file="imagens/botao_estatisticas.png")
    imagem_botao_sair = tk.PhotoImage(file="imagens/botao_sair.png")



def carregar_telas():
    global resto_tela

    resto_tela = tk.Frame(janela,bg=cor_fundo)
    resto_tela.place(relx=0.2,rely=0,relwidth=0.8,relheight=1)

def carregar_menu(mudar_tela):
    menu = tk.Frame(janela,bg=cor_fundo)
    menu.place(relx=0,rely=0,relwidth=0.2,relheight=1)


    menu_lateral = tk.Label(menu,image=imagem_menu_lateral,bg=cor_fundo)
    menu_lateral.place(relx=0,rely=0)

    botao_inicio = tk.Button(menu,image=imagem_botao_inicio,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(1))
    botao_inicio.place(relx = 0.1, rely = 0.15)

    botao_materias = tk.Button(menu,image=imagem_botao_materias,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(2))
    botao_materias.place(relx = 0.1, rely = 0.22)

    botao_tarefas = tk.Button(menu,image=imagem_botao_tarefas,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(3))
    botao_tarefas.place(relx = 0.1, rely = 0.29)

    botao_planejamento=tk.Button(menu,image=imagem_botao_planejamento,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(4))
    botao_planejamento.place(relx = 0.1, rely = 0.36)

    botao_cronometro=tk.Button(menu,image=imagem_botao_cronometro,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(5))
    botao_cronometro.place(relx = 0.1, rely = 0.43)

    botao_historico=tk.Button(menu,image=imagem_botao_historico,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(6))
    botao_historico.place(relx = 0.1, rely = 0.50)

    botao_estatisticas=tk.Button(menu,image=imagem_botao_estatisticas,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(7))
    botao_estatisticas.place(relx = 0.1, rely = 0.57)

    botao_sair=tk.Button(menu,image=imagem_botao_sair,relief="flat",highlightthickness=0,bg=cor_fundo_botao,command= lambda:mudar_tela(-1))
    botao_sair.place(relx = 0.1, rely = 0.9)



def cadastrar_nova_materia(materias):
    for widget in resto_tela.winfo_children():
        widget.destroy()


    tela_cadastro_materia = tk.Label(resto_tela,image=imagem_tela_cadastro_materia)
    tela_cadastro_materia.place(x=0,y=0)

    entrada_nome = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_nome.place(x=300,y=200)

    entrada_descricao = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_descricao.place(x=347,y=315)

    botao_confirmar = tk.Button(resto_tela,image=imagem_botao_confirmar,command=lambda: (gerenciamento_materias.cadastrar_materia(materias,entrada_nome.get(),entrada_descricao.get()),interface(2,materias)))    
    botao_confirmar.place(x=500,y=650)

def mostrar_materias(materias):
    lista_materias = gerenciamento_materias.listar_materias(materias)

    for i, materia in enumerate(lista_materias):
        botao_materia = tk.Button(resto_tela,text=materia["nome"],font=fonte_palavras,anchor="w",relief="flat",bd=0,bg=cor_branca,activebackground=cor_branca,command=lambda m=materia: (nome_materia.config(text=f"Nome: {m['nome']}"),print_id_materia.config(text=f"Id: {m['id']}"),print_detalhes_materia.config(text=f"Descrição:{m['descricao']}")))
        botao_materia.place(x=40,y=100+i*40)

def interface(tela,materias=None):
    global nome_materia
    global print_id_materia
    global print_detalhes_materia

    if tela == 1:
        fundo = tk.Label(resto_tela,bg=cor_fundo,image=imagem_tela_inicial)
        fundo.place(x=0,y=0)
        
    elif tela == 2:
        
        

        painel_materias = tk.Label(resto_tela,image=imagem_tela_materias)
        painel_materias.place(x=0,y=0)

        botao_cadastro_materias = tk.Button(resto_tela,image=imagem_botao_cadastro_materias,relief="flat",bd=0,highlightthickness=0,command=lambda:cadastrar_nova_materia(materias))
        botao_cadastro_materias.place(relx=0.045,rely=0.85)

        nome_materia = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        nome_materia.place(x=500,y=100)

        print_id_materia = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        print_id_materia.place(x=500,y=150)

        print_detalhes_materia = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca,wraplength=400,justify="left")
        print_detalhes_materia.place(x=500,y=200)
        mostrar_materias(materias)

        
    elif tela ==3:
        background = tk.Label(resto_tela,image=imagem_fundo)
        background.place(x=0,y=0)
    elif tela ==4:
        background = tk.Label(resto_tela,image=imagem_fundo)
        background.place(x=0,y=0)
    elif tela ==5:
        background = tk.Label(resto_tela,image=imagem_tela_cronometro)
        background.place(x=0,y=0)

        botao_pause = tk.Button(resto_tela,image=imagem_botao_pause)
        botao_pause.place(relx=0.44,rely=0.2)

        botao_reload = tk.Button(resto_tela,image=imagem_botao_reload)
        botao_reload.place(relx=0.24,rely=0.2)
        botao_pomodoro = tk.Button(resto_tela,image=imagem_botao_pomodoro)
        botao_pomodoro.place(relx=0.64,rely=0.2)
    elif tela ==6:
        background = tk.Label(resto_tela,image=imagem_fundo)
        background.place(x=0,y=0)
    elif tela ==7:
        background = tk.Label(resto_tela,image=imagem_fundo)
        background.place(x=0,y=0)




        