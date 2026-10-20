import tkinter as tk
import interface
import gerenciamento_materias

tela = 1
materias = [
    {"id": 1, "nome": "Cálculo B"},
    {"id": 2, "nome": "Álgebra Linear"},
    {"id": 3, "nome": "Física 1"}
]

def mudar_tela(nova_tela):
    global tela

    if nova_tela == -1:
        interface.janela.destroy()
        return

    tela = nova_tela
    
    for widget in interface.resto_tela.winfo_children():
        widget.destroy()

    interface.interface(tela,materias)

interface.janela = tk.Tk()
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.resizable(False, False)
interface.janela.configure(bg=interface.cor_fundo)

interface.carregar_menu(mudar_tela)
interface.carregar_telas()
interface.interface(tela,materias)

interface.janela.mainloop()