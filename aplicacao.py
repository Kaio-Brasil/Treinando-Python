import tkinter as tk
from telaDoGame import *
import jogoAdivinhe

raiz = tk.Tk()
LARGURA = 800
ALTURA = 500
LARGURA_SCREEN = raiz.winfo_screenwidth()
ALTURA_SCREEN = raiz.winfo_screenheight()
POSX = LARGURA_SCREEN/2 - LARGURA/2
POSY = ALTURA_SCREEN/2 - ALTURA/2

class Aplicacao: 
    def __init__(self):
        self.raiz = raiz
        self.tela()
        self.frameDaTelaPrincipal()
        self.conteudoDoFrameDaTelaPrincipal()
        raiz.mainloop()

    def tela(self):
        raiz.geometry('%dx%d+%d+%d'%(LARGURA, ALTURA, POSX, POSY))
        raiz.title('App Adivinha')
        raiz.config(bg='#808080')
        raiz.resizable(width=False, height=False)
    
    def telaPlayer1(self):
        tg = TelaDoGame()
        tg.criarTela()
        
    def telaPlayer2(self):
        telaPlayer2 = tk.Toplevel()
        telaPlayer2.geometry('%dx%d+%d+%d'%(LARGURA, ALTURA, POSX, POSY))
        telaPlayer2.title('App Adivinha')
        telaPlayer2.config(bg='#808080')
        telaPlayer2.resizable(width=False, height=False)
        telaPlayer2.transient(self.raiz)
        telaPlayer2.focus_force()
        telaPlayer2.grab_set()

    def tela2(self):
        if self.modoJogo.get():
            self.telaPlayer2()            
        else:
            self.telaPlayer1()

    def frameDaTelaPrincipal(self):
        self.framePrincipal = tk.Frame(self.raiz, bd=2, bg='#dcdcdc', highlightbackground='#ffffff', 
                 highlightthickness=2).place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.9)

    def conteudoDoFrameDaTelaPrincipal(self):
        self.modoJogo = tk.BooleanVar()

        #Titulo da minha aplicação
        tk.Label(self.framePrincipal, text='Jogo Adivinha', bg='#dcdcdc', fg='#ff4500', 
                 font=('verdana', 24, 'bold')).place(relx=0.34, rely=0.08)

        #Frame da aplicacao principal
        frameDaAplicacao = tk.Frame(self.framePrincipal, width=700, height=320, bd=2, bg='#dcdcdc', 
                 highlightbackground='#111111', highlightthickness=2).place(relx=0.06, rely=0.23)

        #Texto da pergunta modo do jogo
        tk.Label(frameDaAplicacao, text='Escola o modo de jogo que deseja jogar?', 
                 bg='#dcdcdc', fg='#000000', font=('arial', 18)).place(relx=0.22, rely=0.32)

        tk.Radiobutton(frameDaAplicacao, text='1 Player', font=('arial', 14), value=False, 
                       variable=self.modoJogo, bg='#dcdcdc').place(relx=0.3, rely=0.47)

        tk.Radiobutton(frameDaAplicacao, text='2 Player', font=('arial', 14), value=True, 
                       variable=self.modoJogo, bg='#dcdcdc').place(relx=0.55, rely=0.47)

        tk.Button(frameDaAplicacao, text='Seguir', bg='#dcdcdc', fg='#000000', font=('arial', 14, 'bold'), 
                  padx=16, pady=4, command=self.tela2).place(relx=0.77, rely=0.73)

aplicacao = Aplicacao()