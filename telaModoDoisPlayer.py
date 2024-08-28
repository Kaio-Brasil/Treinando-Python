import tkinter as tk
from screenDisplay import *

class TelaModoDoisPlayer(ScreenDisplay):        
    def criarTelaModoDois(self):
        self.tela2Player = tk.Toplevel()
        dimencoes = self.dimencoesDeTela( self.tela2Player.winfo_screenwidth, self.tela2Player.winfo_screenheight)
        self.tela2Player.geometry('%dx%d+%d+%d'%(dimencoes[0], dimencoes[1], dimencoes[2], dimencoes[3]))
        self.tela2Player.geometry('800x500')
        self.tela2Player.title('App Adivinha')
        self.tela2Player.config(bg='#808080')
        self.tela2Player.resizable(width=False, height=False)
        self.tela2Player.transient(self.raiz)
        self.tela2Player.focus_force()
        self.tela2Player.grab_set()

    def fechar(self):
        self.tela2Player.destroy()
        self.tela2Player = None