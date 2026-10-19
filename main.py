import tkinter as tk
import interface



tela = 1 
def mudar_tela(nova_tela):
    global tela

    if nova_tela == -1: 
        interface.janela.destroy()
        return

    tela = nova_tela 

    for widget in interface.resto_tela.winfo_children():
        widget.destroy()

    interface.interface(tela)

interface.janela = tk.Tk()
interface.carregar_imagens()
interface.janela.geometry(f"{interface.largura}x{interface.altura}")
interface.janela.resizable(False, False)
interface.janela.configure(bg=interface.cor_fundo)


interface.carregar_menu(mudar_tela)
interface.carregar_conteudo()
interface.interface(tela)
interface.janela.mainloop()