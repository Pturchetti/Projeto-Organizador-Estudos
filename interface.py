
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
#tela 5 -cronometro
#tela 6 -histórico
#tela 7 -estatísticas


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

janela = None
resto_tela = None

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

def interface(tela):

    if tela == 1:
        fundo = tk.Label(resto_tela,bg=cor_fundo,image=imagem_tela_inicial)
        fundo.place(x=0,y=0)
        
    elif tela == 2:
        background = tk.Label(resto_tela,image=imagem_fundo)
        background.place(x=0,y=0)
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




        