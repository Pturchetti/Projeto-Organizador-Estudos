import tkinter as tk
import interface
import gerenciamento_materias
import persistencia
import historico

tela = 1
materias = persistencia.carregar("materias")
tarefas = persistencia.carregar("tarefas")
dias_historico = persistencia.carregar("historico")

def mudar_tela(nova_tela):
    global tela
    persistencia.salvar("materias", materias)
    persistencia.salvar("tarefas", tarefas)
    persistencia.salvar("historico", dias_historico)
    interface.controlar_pomodoro("encerrar")

    if nova_tela == -1:
        interface.janela.destroy()
        return

    tela = nova_tela
    
    for widget in interface.resto_tela.winfo_children():
        widget.destroy()

    interface.interface(tela,materias,dias_historico,lambda: persistencia.salvar("historico", dias_historico))

interface.janela = tk.Tk()
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.resizable(False, False)
interface.janela.configure(bg=interface.cor_fundo)

interface.carregar_menu(mudar_tela)
interface.carregar_telas()
interface.interface(tela,materias,dias_historico,lambda: persistencia.salvar("historico", dias_historico))

interface.janela.mainloop()