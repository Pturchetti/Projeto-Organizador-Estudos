import tkinter as tk
from tkinter import messagebox, ttk
import gerenciamento_materias
import gerenciamento_tarefas
import historico
import cronometro
from datetime import date, datetime, timedelta
import planejamento_semanal

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
janela = None
resto_tela = None
nome_materia = None
id_materia = None
print_detalhes_materia = None

nome_tarefa = None
print_id_tarefa = None
print_detalhes_tarefa = None

pomodoro_atual = None
pomodoro_job = None
rotulo_tempo_pomodoro = None
rotulo_modo_pomodoro = None
rotulo_status_pomodoro = None
entrada_foco_pomodoro = None
entrada_descanso_pomodoro = None
historico_pomodoro = None
salvar_historico_pomodoro = None

def encerrar_cronometro():
    global pomodoro_job
    if pomodoro_job is not None and janela is not None:
        janela.after_cancel(pomodoro_job)
        pomodoro_job = None
    if pomodoro_atual is not None:
        pomodoro_atual.pausar()

def atualizar_pomodoro():
    rotulo_tempo_pomodoro.config(text=cronometro.formatar_tempo(pomodoro_atual.segundos_restantes))
    rotulo_modo_pomodoro.config(text=f"Período de {pomodoro_atual.modo}")

def aplicar_tempos_pomodoro():
    if pomodoro_atual.executando:
        pausar_pomodoro()
    try:
        pomodoro_atual.configurar(entrada_foco_pomodoro.get(), entrada_descanso_pomodoro.get())
    except ValueError as erro:
        messagebox.showerror("Tempos inválidos", str(erro))
        return
    atualizar_pomodoro()
    rotulo_status_pomodoro.config(text="Tempos aplicados. Pronto para iniciar.")

def iniciar_pomodoro():
    global pomodoro_job
    if not pomodoro_atual.executando:
        pomodoro_atual.iniciar()
        rotulo_status_pomodoro.config(text="Cronômetro em andamento.")
        pomodoro_job = janela.after(1000, avancar_pomodoro)

def pausar_pomodoro():
    global pomodoro_job
    pomodoro_atual.pausar()
    if pomodoro_job is not None:
        janela.after_cancel(pomodoro_job)
        pomodoro_job = None
    rotulo_status_pomodoro.config(text="Cronômetro pausado.")

def reiniciar_pomodoro():
    global pomodoro_job
    pomodoro_atual.reiniciar()
    if pomodoro_job is not None:
        janela.after_cancel(pomodoro_job)
        pomodoro_job = None
    atualizar_pomodoro()
    rotulo_status_pomodoro.config(text="Período reiniciado.")

def avancar_pomodoro():
    global pomodoro_job
    pomodoro_job = None
    modo_concluido = pomodoro_atual.avancar_segundo()
    if modo_concluido == "foco":
        historico.registrar_sessao_pomodoro(historico_pomodoro, pomodoro_atual.foco_minutos)
        salvar_historico_pomodoro()
        rotulo_status_pomodoro.config(text="Foco concluído! Hora de descansar.")
    elif modo_concluido == "descanso":
        rotulo_status_pomodoro.config(text="Descanso concluído! Vamos focar.")
    atualizar_pomodoro()
    pomodoro_job = janela.after(1000, avancar_pomodoro)

def carregar_imagens():
    global imagem_tela_inicial, imagem_botao_inicio, imagem_botao_materias, imagem_botao_tarefas
    global imagem_botao_planejamento, imagem_botao_cronometro, imagem_botao_historico
    global imagem_botao_estatisticas, imagem_botao_sair, imagem_fundo, imagem_menu_lateral
    global imagem_balao_tarefas, imagem_botao_pause, imagem_botao_reload, imagem_botao_pomodoro
    global imagem_tela_cronometro, imagem_tela_materias, imagem_botao_cadastro_materias
    global imagem_tela_cadastro_materia, imagem_botao_confirmar, imagem_botao_editar_materia
    global imagem_botao_remover_materia, imagem_tela_procura, imagem_tela_edicao, imagem_tela_historico
    global imagem_tela_planejamento, imagem_botao_editar_planejamento
    
    global imagem_tela_tarefas, imagem_botao_cadastrar_tarefa, imagem_botao_editar_tarefa
    global imagem_botao_remover_tarefa, imagem_botao_concluir_tarefa

    imagem_tela_historico = tk.PhotoImage(file="imagens/tela_historico.png")
    imagem_botao_editar_materia = tk.PhotoImage(file="imagens/botao_editar_materia.png")
    imagem_botao_remover_materia = tk.PhotoImage(file="imagens/botao_remover_materia.png")
    imagem_tela_procura = tk.PhotoImage(file="imagens/tela_procura.png")
    imagem_tela_edicao = tk.PhotoImage(file="imagens/tela_edicao.png")
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
    imagem_tela_planejamento = tk.PhotoImage(file="imagens/tela_planejamento.png")
    imagem_botao_editar_planejamento = tk.PhotoImage(file="imagens/botao_editar_planejamento.png")
    
    # Imagens de tarefas (mesmas nomes que estavam no zip)
    try:
        imagem_tela_tarefas = tk.PhotoImage(file="imagens/tela_tarefas.png")
    except tk.TclError:
        imagem_tela_tarefas = imagem_tela_materias # fallback caso não exista a imagem específica
        
    imagem_botao_cadastrar_tarefa = tk.PhotoImage(file="imagens/botao_cadastrar_terefa.png") 
    imagem_botao_editar_tarefa = tk.PhotoImage(file="imagens/botao_editar_tarefa.png")
    imagem_botao_remover_tarefa = tk.PhotoImage(file="imagens/botao_remover_tarefa.png")
    imagem_botao_concluir_tarefa = tk.PhotoImage(file="imagens/botao_concluir_tarefa.png")


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


def remover_materia_tela(materias, dias_historico, salvar_historico, tarefas):
    for widget in resto_tela.winfo_children():
        widget.destroy()
    tela_procura = tk.Label(resto_tela,image=imagem_tela_procura)
    tela_procura.place(x=0,y=0)
    entrada_id = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_id.place(x=70,y=200)

    botao_confirmar = tk.Button(resto_tela,image=imagem_botao_confirmar,command=lambda: (gerenciamento_materias.remover_materia(materias,int(entrada_id.get())),interface(2,materias,dias_historico,salvar_historico,tarefas)))
    botao_confirmar.place(x=500,y=650)

def editar_materia_tela(materias, dias_historico, salvar_historico, tarefas):
    for widget in resto_tela.winfo_children():
        widget.destroy()
    tela_edicao = tk.Label(resto_tela,image=imagem_tela_edicao)
    tela_edicao.place(x=0,y=0)
    entrada_id = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_id.place(x=70,y=100)
    entrada_nome = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_nome.place(x=200,y=205)
    entrada_descricao = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_descricao.place(x=250,y=320)

    botao_confirmar = tk.Button(resto_tela,image=imagem_botao_confirmar,command=lambda: (gerenciamento_materias.editar_materia(materias,int(entrada_id.get()),entrada_nome.get(),entrada_descricao.get()),interface(2,materias,dias_historico,salvar_historico,tarefas)))
    botao_confirmar.place(x=500,y=650)

def cadastrar_nova_materia(materias, dias_historico, salvar_historico, tarefas):
    for widget in resto_tela.winfo_children():
        widget.destroy()
    tela_cadastro_materia = tk.Label(resto_tela,image=imagem_tela_cadastro_materia)
    tela_cadastro_materia.place(x=0,y=0)
    entrada_nome = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_nome.place(x=300,y=200)
    entrada_descricao = tk.Entry(resto_tela,font=fonte_palavras)
    entrada_descricao.place(x=347,y=315)

    botao_confirmar = tk.Button(resto_tela,image=imagem_botao_confirmar,command=lambda: (gerenciamento_materias.cadastrar_materia(materias,entrada_nome.get(),entrada_descricao.get()),interface(2,materias,dias_historico,salvar_historico,tarefas)))    
    botao_confirmar.place(x=500,y=650)

def mostrar_materias(materias):
    lista_materias = gerenciamento_materias.listar_materias(materias)
    for i, materia in enumerate(lista_materias):
        botao_materia = tk.Button(resto_tela,text=materia["nome"],font=fonte_palavras,anchor="w",relief="flat",bd=0,bg=cor_branca,activebackground=cor_branca,command=lambda m=materia: (nome_materia.config(text=f"Nome: {m['nome']}"),print_id_materia.config(text=f"Id: {m['id']}"),print_detalhes_materia.config(text=f"Descrição:{m['descricao']}")))
        botao_materia.place(x=40,y=100+i*40)


def remover_tarefa_tela(tarefas, materias, dias_historico, salvar_historico):
    for widget in resto_tela.winfo_children():
        widget.destroy()

    tela_procura = tk.Label(resto_tela, image=imagem_tela_procura)
    tela_procura.place(x=0, y=0)
    
    entrada_id = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_id.place(x=70, y=200)

    botao_confirmar = tk.Button(resto_tela, image=imagem_botao_confirmar, command=lambda: (gerenciamento_tarefas.remover_tarefa(tarefas, int(entrada_id.get())), interface(3, materias, dias_historico, salvar_historico, tarefas)))
    botao_confirmar.place(x=500, y=650)

def editar_tarefa_tela(tarefas, materias, dias_historico, salvar_historico):
    for widget in resto_tela.winfo_children():
        widget.destroy()

    tela_edicao = tk.Label(resto_tela, image=imagem_tela_edicao)
    tela_edicao.place(x=0, y=0)
    
    entrada_id_tarefa = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_id_tarefa.place(x=70, y=100)
    entrada_id_materia = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_id_materia.place(x=200, y=205)
    entrada_titulo = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_titulo.place(x=250, y=320)
    entrada_descricao = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_descricao.place(x=250, y=435)

    def confirmar_edicao():
        try:
            gerenciamento_tarefas.editar_tarefa(
                tarefas, 
                int(entrada_id_tarefa.get()), 
                entrada_id_materia.get(), 
                entrada_titulo.get(), 
                entrada_descricao.get()
            )
            interface(3, materias, dias_historico, salvar_historico, tarefas)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    botao_confirmar = tk.Button(resto_tela, image=imagem_botao_confirmar, command=confirmar_edicao)
    botao_confirmar.place(x=500, y=650)

def cadastrar_nova_tarefa(tarefas, materias, dias_historico, salvar_historico):
    for widget in resto_tela.winfo_children():
        widget.destroy()

    tela_cadastro = tk.Label(resto_tela, image=imagem_tela_cadastro_materia)
    tela_cadastro.place(x=0, y=0)
    
    entrada_id_materia = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_id_materia.place(x=300, y=100) 
    entrada_titulo = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_titulo.place(x=300, y=200) 
    entrada_descricao = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_descricao.place(x=300, y=320)

    def confirmar_cadastro():
        try:
            gerenciamento_tarefas.cadastrar_tarefa(
                tarefas, 
                entrada_id_materia.get(), 
                entrada_titulo.get(), 
                entrada_descricao.get()
            )
            interface(3, materias, dias_historico, salvar_historico, tarefas)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    botao_confirmar = tk.Button(resto_tela, image=imagem_botao_confirmar, command=confirmar_cadastro)    
    botao_confirmar.place(x=500, y=650)

def concluir_tarefa_tela(tarefas, materias, dias_historico, salvar_historico):
    for widget in resto_tela.winfo_children():
        widget.destroy()

    tela_procura = tk.Label(resto_tela, image=imagem_tela_procura)
    tela_procura.place(x=0, y=0)
    
    entrada_id = tk.Entry(resto_tela, font=fonte_palavras)
    entrada_id.place(x=70, y=200)

    def confirmar_conclusao():
        try:
            id_t = int(entrada_id.get())
            gerenciamento_tarefas.concluir_tarefa(tarefas, id_t)
            historico.registrar_tarefa_concluida(dias_historico, id_t)
            salvar_historico()
            interface(3, materias, dias_historico, salvar_historico, tarefas)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    botao_confirmar = tk.Button(resto_tela, image=imagem_botao_confirmar, command=confirmar_conclusao)
    botao_confirmar.place(x=500, y=650)

def mostrar_tarefas(tarefas):
    lista_tarefas = gerenciamento_tarefas.listar_tarefas(tarefas)
    for i, tarefa in enumerate(lista_tarefas):
        status = "Concluída" if tarefa.get("concluida") else "Pendente"
        descricao_fmt = tarefa.get("descricao") if tarefa.get("descricao") else "Sem descrição"
        
        texto_detalhes = f"Matéria ID: {tarefa.get('id_materia')}\nDescrição: {descricao_fmt}\nStatus: {status}"
        
        botao_tarefa = tk.Button(resto_tela, text=tarefa["titulo"], font=fonte_palavras, anchor="w", relief="flat", bd=0, bg=cor_branca, activebackground=cor_branca, 
                                 command=lambda t=tarefa, txt=texto_detalhes: (nome_tarefa.config(text=f"Título: {t['titulo']}"), print_id_tarefa.config(text=f"Id: {t['id']}"), print_detalhes_tarefa.config(text=txt)))
        botao_tarefa.place(x=40, y=100+i*40)


def mostrar_historico(dias_historico):
    for i, dia in enumerate(dias_historico):
        botao_dia = tk.Button(resto_tela,text=dia["data"],font=fonte_palavras,anchor="w",relief="flat",bd=0,bg=cor_branca,activebackground=cor_branca,command=lambda d=dia: (nome_dia_historico.config(text=f"Data: {d['data']} - {d['dia_semana']}"),horas_historico.config(text=f"Tempo estudado: {d['horas_estudadas']}"),tarefas_historico.config(text=f"Tarefas concluídas: {len(d['tarefas_feitas'])}"),sessoes_historico.config(text=f"Sessões Pomodoro concluídas: {d.get('sessoes_pomodoro', 0)}")))
        botao_dia.place(x=40,y=100+i*40)

def editar_dia_planejamento(data, materias, dias_historico, salvar_historico, tarefas):
    janela_edicao = tk.Toplevel(janela)
    janela_edicao.title("Planejamento do dia")
    janela_edicao.geometry("650x500")
    janela_edicao.configure(bg=cor_fundo)

    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"    ]
    data_obj = datetime.strptime(data, "%Y-%m-%d")
    tk.Label(janela_edicao,text=f"{data_obj.day} de {meses[data_obj.month - 1]} de {data_obj.year}",font=("Inter", 18, "bold"),bg=cor_fundo).pack(pady=12)
    tk.Label(janela_edicao,text="Planejamentos:",font=("Inter", 14, "bold"),bg=cor_fundo).pack()
    lista_frame = tk.Frame(janela_edicao, bg=cor_fundo)
    lista_frame.pack(fill="both", expand=True, padx=15, pady=10)

    def atualizar_lista():
        for widget in lista_frame.winfo_children():
            widget.destroy()

        lista = planejamento_semanal.listar_dia(data)

        if not lista:
            tk.Label(
                lista_frame,
                text="Nada previsto.",
                bg=cor_fundo,
                font=("Inter", 12)
            ).pack(pady=10)
            return

        for p in lista:
            materia = gerenciamento_materias.buscar_materia(
                materias, p["materia_id"]
            )
            nome = materia["nome"] if materia else "Matéria removida"

            linha = tk.Frame(lista_frame, bg=cor_branca)
            linha.pack(fill="x", pady=4)

            texto = (
                f'{p["horario"]} | {nome} | '
                f'{p["duracao"]} min\n{p["descricao"]}'
            )

            tk.Label(linha,text=texto,bg=cor_branca,justify="left",anchor="w").pack(side="left", padx=8, pady=6, fill="x", expand=True)
            tk.Button(linha,text="Remover",command=lambda item=p: remover(item)).pack(side="right", padx=8)

        def remover(p):
            if messagebox.askyesno(
            "Confirmar",
            "Deseja remover este planejamento?",
            parent=janela_edicao
            ):
                planejamento_semanal.remover_planejamento(p["id"])

            janela_edicao.destroy()

            for widget in resto_tela.winfo_children():
                widget.destroy()

            interface(4, materias, dias_historico, salvar_historico, tarefas)

    def adicionar():
        if not materias:
            messagebox.showerror(
                "Sem matérias",
                "Cadastre uma matéria antes de planejar.",
                parent=janela_edicao
            )
            return

        formulario = tk.Toplevel(janela_edicao)
        formulario.title("Adicionar planejamento")
        formulario.geometry("350x390")
        formulario.configure(bg=cor_fundo)

        tk.Label(formulario,text="Horário",bg=cor_fundo).pack(pady=(10, 0))

        horarios = [
            f"{h:02d}:{m:02d}"
            for h in range(24)
            for m in range(0, 60, 15)
        ]

        horario_var = tk.StringVar(value="08:00")

        seletor_horario = ttk.Combobox(formulario,textvariable=horario_var,values=horarios,state="readonly",height=6,width=10        )
        seletor_horario.pack()

        tk.Label(formulario,text="Duração",bg=cor_fundo).pack(pady=(10, 0))
        duracao_var = tk.StringVar(value="00:30")

        tk.OptionMenu(formulario,duracao_var,"00:15", "00:30", "00:45", "01:00","01:15", "01:30", "01:45", "02:00").pack()

        tk.Label(formulario,text="Matéria",bg=cor_fundo).pack(pady=(10, 0))

        materias_lista = gerenciamento_materias.listar_materias(materias)
        nomes = [m["nome"] for m in materias_lista]
        materia_var = tk.StringVar(value=nomes[0])

        tk.OptionMenu(formulario,materia_var,*nomes).pack()

        tk.Label(formulario,text="Descrição",bg=cor_fundo).pack(pady=(10, 0))

        entrada_descricao = tk.Entry(formulario, width=35)
        entrada_descricao.pack()

        def salvar_planejamento():
            try:
                horario = horario_var.get()
                horas, minutos = map(
                    int,
                    duracao_var.get().split(":")
                )
                duracao = horas * 60 + minutos
                materia = next(
                    m for m in materias_lista
                    if m["nome"] == materia_var.get()
                )

                planejamento_semanal.adicionar_planejamento(data,horario,duracao,materia["id"],entrada_descricao.get().strip())

            except ValueError as erro:
                messagebox.showerror(
                    "Erro",
                    str(erro),
                    parent=formulario
                )
                return

            formulario.destroy()
            janela_edicao.destroy()

            for widget in resto_tela.winfo_children():
                widget.destroy()

            interface(4, materias, dias_historico, salvar_historico, tarefas)

        tk.Button(formulario,text="Salvar",command=salvar_planejamento).pack(pady=15)
    tk.Button(janela_edicao,text="Adicionar",command=adicionar).pack(pady=(0, 12))
    atualizar_lista()

def interface(tela,materias=None,dias_historico=None,salvar_historico=None, tarefas=None):
    global nome_materia, print_id_materia, print_detalhes_materia
    global nome_tarefa, print_id_tarefa, print_detalhes_tarefa
    global nome_dia_historico, horas_historico, tarefas_historico, sessoes_historico
    global pomodoro_atual, rotulo_tempo_pomodoro, rotulo_modo_pomodoro, rotulo_status_pomodoro
    global entrada_foco_pomodoro, entrada_descanso_pomodoro
    global historico_pomodoro, salvar_historico_pomodoro

    if tela == 1:
        fundo = tk.Label(resto_tela,bg=cor_fundo,image=imagem_tela_inicial)
        fundo.place(x=0,y=0)
        
    elif tela == 2:
        painel_materias = tk.Label(resto_tela,image=imagem_tela_materias)
        painel_materias.place(x=0,y=0)

        botao_editar_materia = tk.Button(resto_tela,image=imagem_botao_editar_materia,relief="flat",bd=0,highlightthickness=0,command=lambda: editar_materia_tela(materias, dias_historico, salvar_historico, tarefas))
        botao_editar_materia.place(relx=0.045,rely=0.70)

        botao_remover_materia = tk.Button(resto_tela,image=imagem_botao_remover_materia,relief="flat",bd=0,highlightthickness=0,command=lambda: remover_materia_tela(materias, dias_historico, salvar_historico, tarefas))
        botao_remover_materia.place(relx=0.045,rely=0.775)

        botao_cadastro_materias = tk.Button(resto_tela,image=imagem_botao_cadastro_materias,relief="flat",bd=0,highlightthickness=0,command=lambda:cadastrar_nova_materia(materias, dias_historico, salvar_historico, tarefas))
        botao_cadastro_materias.place(relx=0.045,rely=0.85)

        nome_materia = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        nome_materia.place(x=500,y=100)

        print_id_materia = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        print_id_materia.place(x=500,y=150)

        print_detalhes_materia = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca,wraplength=400,justify="left")
        print_detalhes_materia.place(x=500,y=200)
        mostrar_materias(materias)

    elif tela == 3:
        painel_tarefas = tk.Label(resto_tela, image=imagem_tela_tarefas)
        painel_tarefas.place(x=0, y=0)

        botao_concluir = tk.Button(resto_tela, image=imagem_botao_concluir_tarefa, relief="flat", bd=0, highlightthickness=0, command=lambda: concluir_tarefa_tela(tarefas, materias, dias_historico, salvar_historico))
        botao_concluir.place(relx=0.045, rely=0.625)

        botao_editar = tk.Button(resto_tela, image=imagem_botao_editar_tarefa, relief="flat", bd=0, highlightthickness=0, command=lambda: editar_tarefa_tela(tarefas, materias, dias_historico, salvar_historico))
        botao_editar.place(relx=0.045, rely=0.70)

        botao_remover = tk.Button(resto_tela, image=imagem_botao_remover_tarefa, relief="flat", bd=0, highlightthickness=0, command=lambda: remover_tarefa_tela(tarefas, materias, dias_historico, salvar_historico))
        botao_remover.place(relx=0.045, rely=0.775)

        botao_cadastro = tk.Button(resto_tela, image=imagem_botao_cadastrar_tarefa, relief="flat", bd=0, highlightthickness=0, command=lambda: cadastrar_nova_tarefa(tarefas, materias, dias_historico, salvar_historico))
        botao_cadastro.place(relx=0.045, rely=0.85)

        nome_tarefa = tk.Label(resto_tela, text="", font=fonte_titulo, bg=cor_branca)
        nome_tarefa.place(x=500, y=100)
        print_id_tarefa = tk.Label(resto_tela, text="", font=fonte_titulo, bg=cor_branca)
        print_id_tarefa.place(x=500, y=150)
        print_detalhes_tarefa = tk.Label(resto_tela, text="", font=fonte_titulo, bg=cor_branca, wraplength=400, justify="left")
        print_detalhes_tarefa.place(x=500, y=200)
        
        mostrar_tarefas(tarefas)
        
    elif tela == 4:
        background = tk.Label(resto_tela,image=imagem_tela_planejamento)
        background.place(x=0, y=0)
        inicio_semana = date.today() - timedelta(days=date.today().weekday())
        semana = planejamento_semanal.listar_semana(inicio_semana)

        for i, dia in enumerate(semana):            
            if i == 0:  
                x = 55
                y = 140
            elif i == 1:
                x = 348
                y = 140
            elif i == 2:
                x = 632
                y = 140
            elif i == 3:
                x = 918
                y = 140
            elif i == 4:
                x = 204
                y = 440
            elif i == 5:
                x = 490
                y = 440
            elif i == 6:
                x = 784
                y = 440

            lista_periodos = dia["planejamentos"]

            if lista_periodos:
                texto = "\n".join(
                    p["horario"] + " - " +
                    (p["descricao"] or "Estudo") +
                    " (" + str(p["duracao"]) + " min)"
                    for p in lista_periodos
                )
            else:
                texto = "Nenhum período planejado"
            tk.Label(resto_tela,text=texto,font=("Inter", 10),bg=cor_branca,fg=cor_fundo_botao,wraplength=250,justify="center").place(x=x + 35, y=y - 50, width=210, height=110)
            tk.Button(resto_tela,text="Editar",font=("Inter", 12, "bold"),bg=cor_branca,fg=cor_fundo_botao,activebackground=cor_branca,activeforeground=cor_fundo_botao,relief="flat",bd=0,cursor="hand2",command=lambda d=dia["data"]: editar_dia_planejamento(d, materias, dias_historico, salvar_historico, tarefas)).place(x=x + 100, y=y + 125, width=80, height=28)
            
    elif tela ==5:
        background = tk.Label(resto_tela,image=imagem_tela_cronometro)
        background.place(x=0,y=0)
        painel_pomodoro = tk.Frame(resto_tela,bg=cor_fundo_botao,bd=0,highlightthickness=0)
        painel_pomodoro.place(x=30,y=410,width=1220,height=475)

        pomodoro_atual = cronometro.Pomodoro()
        historico_pomodoro = dias_historico
        salvar_historico_pomodoro = salvar_historico

        configuracao_pomodoro = tk.Frame(resto_tela,bg=cor_fundo)
        configuracao_pomodoro.place(relx=0.5,rely=0.04,anchor="n")
        tk.Label(configuracao_pomodoro,text="Duração dos períodos (minutos)",font=("Inter",20,"bold"),fg=cor_fundo_botao,bg=cor_fundo).pack(pady=(0,10))

        campos_duracao_pomodoro = tk.Frame(configuracao_pomodoro,bg=cor_fundo)
        campos_duracao_pomodoro.pack()
        tk.Label(campos_duracao_pomodoro,text="Foco",font=("Inter",16,"bold"),fg=cor_fundo_botao,bg=cor_fundo).grid(row=0,column=0,padx=(0,8))
        entrada_foco_pomodoro = tk.Entry(campos_duracao_pomodoro,font=("Inter",16,"bold"),width=6,justify="center",relief="flat",bd=0,bg=cor_branca,fg=cor_fundo_botao,insertbackground=cor_fundo_botao)
        entrada_foco_pomodoro.insert(0,str(pomodoro_atual.foco_minutos))
        entrada_foco_pomodoro.grid(row=0,column=1,padx=(0,24))
        tk.Label(campos_duracao_pomodoro,text="Descanso",font=("Inter",16,"bold"),fg=cor_fundo_botao,bg=cor_fundo).grid(row=0,column=2,padx=(0,8))
        entrada_descanso_pomodoro = tk.Entry(campos_duracao_pomodoro,font=("Inter",16,"bold"),width=6,justify="center",relief="flat",bd=0,bg=cor_branca,fg=cor_fundo_botao,insertbackground=cor_fundo_botao)
        entrada_descanso_pomodoro.insert(0,str(pomodoro_atual.descanso_minutos))
        entrada_descanso_pomodoro.grid(row=0,column=3)
        tk.Button(configuracao_pomodoro,text="Aplicar tempos",font=("Inter",14,"bold"),fg=cor_branca,bg=cor_fundo_botao,activebackground=cor_fundo_botao,activeforeground=cor_branca,relief="flat",bd=0,padx=14,pady=6,cursor="hand2",command=aplicar_tempos_pomodoro).pack(pady=(12,0))

        rotulo_modo_pomodoro = tk.Label(resto_tela,text="Período de foco",font=("Inter",26,"bold"),bg=cor_fundo_botao,fg=cor_branca)
        rotulo_modo_pomodoro.place(relx=0.5,rely=0.50,anchor="center")
        rotulo_tempo_pomodoro = tk.Label(resto_tela,text="25:00",font=("Inter",76,"bold"),bg=cor_fundo_botao,fg=cor_branca)
        rotulo_tempo_pomodoro.place(relx=0.5,rely=0.61,anchor="center")
        rotulo_status_pomodoro = tk.Label(resto_tela,text="Pronto para iniciar o foco.",font=("Inter",16,"bold"),bg=cor_fundo_botao,fg=cor_branca)
        rotulo_status_pomodoro.place(relx=0.5,rely=0.70,anchor="center")

        tk.Button(resto_tela,text="Iniciar",font=("Inter",14,"bold"),fg=cor_branca,bg=cor_fundo_botao,activebackground=cor_fundo_botao,activeforeground=cor_branca,relief="flat",bd=0,padx=12,pady=8,cursor="hand2",command=iniciar_pomodoro).place(relx=0.35,rely=0.79,anchor="center")
        tk.Button(resto_tela,text="Pausar",font=("Inter",14,"bold"),fg=cor_branca,bg=cor_fundo_botao,activebackground=cor_fundo_botao,activeforeground=cor_branca,relief="flat",bd=0,padx=12,pady=8,cursor="hand2",command=pausar_pomodoro).place(relx=0.5,rely=0.79,anchor="center")
        tk.Button(resto_tela,text="Reiniciar",font=("Inter",14,"bold"),fg=cor_branca,bg=cor_fundo_botao,activebackground=cor_fundo_botao,activeforeground=cor_branca,relief="flat",bd=0,padx=12,pady=8,cursor="hand2",command=reiniciar_pomodoro).place(relx=0.65,rely=0.79,anchor="center")
        
    elif tela == 6:
        painel_historico = tk.Label(resto_tela,image=imagem_tela_historico)
        painel_historico.place(x=0,y=0)

        nome_dia_historico = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        nome_dia_historico.place(x=500,y=100)
        horas_historico = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        horas_historico.place(x=500,y=150)
        tarefas_historico = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        tarefas_historico.place(x=500,y=200)
        sessoes_historico = tk.Label(resto_tela,text="",font=fonte_titulo,bg=cor_branca)
        sessoes_historico.place(x=500,y=250)

        mostrar_historico(dias_historico)
        
    elif tela ==7:
        background = tk.Label(resto_tela,image=imagem_fundo)
        background.place(x=0,y=0)
