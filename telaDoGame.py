import tkinter as tk
from aplicacao import *

class TelaDoGame:
    def criarTela(self):
        telaPlayer1 = tk.Toplevel()
        telaPlayer1.geometry('800x500')
        telaPlayer1.title('App Adivinha')
        telaPlayer1.config(bg='#808080')
        telaPlayer1.resizable(width=False, height=False)
        telaPlayer1.transient(self.raiz)
        telaPlayer1.focus_force()
        telaPlayer1.grab_set()
