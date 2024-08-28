import tkinter as tk
from screenDisplay import *

class TelaDoGame(ScreenDisplay):        
    def criarTela(self):
        telaPlayer1 = tk.Toplevel()

        dimencoes = self.dimencoesDeTela(telaPlayer1.winfo_screenwidth, telaPlayer1.winfo_screenheight)
        telaPlayer1.geometry('%dx%d+%d+%d'%(dimencoes[0], dimencoes[1], dimencoes[2], dimencoes[3]))
        telaPlayer1.geometry('800x500')
        telaPlayer1.title('App Adivinha')
        telaPlayer1.config(bg='#808080')
        telaPlayer1.resizable(width=False, height=False)
        telaPlayer1.transient(self.raiz)
        telaPlayer1.focus_force()
        telaPlayer1.grab_set()
