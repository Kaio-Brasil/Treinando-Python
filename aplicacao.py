import tkinter as tk
from telaDoGame import TelaDoGame
from telaModoDoisPlayer import TelaModoDoisPlayer
from screenDisplay import ScreenDisplay
import jogoAdivinhe

class Aplicacao(TelaDoGame, TelaModoDoisPlayer, ScreenDisplay): 
    def __init__(self):
        self.raiz = tk.Tk()
        self.exibindoTela()

    def exibindoTela(self):
        self.tela()
        self.frameDaTelaPrincipal()
        self.conteudoDoFrameDaTelaPrincipal()
        self.raiz.mainloop()

    def tela(self):
        dimencoes = self.dimencoesDeTela(self.raiz.winfo_screenwidth, self.raiz.winfo_screenheight) #Chamada da class screenDisplay
        self.raiz.geometry('%dx%d+%d+%d'%(dimencoes[0], dimencoes[1], dimencoes[2], dimencoes[3]))
        self.raiz.title('App Adivinha')
        self.raiz.config(bg='#808080')
        self.raiz.resizable(width=False, height=False)
    
    #Chamada de funcao da class telaDoGame
    def telaPlayer1(self):
        self.criarTela()
        
    #Chamada de funcao da class telaModoDoisPlayer
    def telaPlayer2(self):
        self.criarTelaModoDois()

    def tela2(self):
        if self.modoJogo.get():
            self.telaPlayer2()            
        else:
            self.telaPlayer1()

    def frameDaTelaPrincipal(self):
        self.framePrincipal = tk.Frame(self.raiz, bd=2, bg='#dcdcdc', highlightbackground='#ffffff', 
                 highlightthickness=2)
        self.framePrincipal.place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.9)

    def conteudoDoFrameDaTelaPrincipal(self):
        self.modoJogo = tk.BooleanVar()

        #Titulo da minha aplicação
        lblTitulo = tk.Label(self.framePrincipal, text='Jogo Adivinha', bg='#dcdcdc', fg='#ff4500', 
                 font=('verdana', 24, 'bold'))
        lblTitulo.place(relx=0.32, rely=0.08)

        #Frame da aplicacao principal
        frameDaAplicacao = tk.Frame(self.framePrincipal, width=700, height=320, bd=2, bg='#dcdcdc', 
                 highlightbackground='#111111', highlightthickness=2)
        frameDaAplicacao.place(relx=0.03, rely=0.23)

        #Texto da pergunta modo do jogo
        lblPerguta = tk.Label(frameDaAplicacao, text='Escola o modo de jogo que deseja jogar?', 
                 bg='#dcdcdc', fg='#000000', font=('arial', 18))
        lblPerguta.place(relx=0.16, rely=0.28)

        #Botão circular de escolha 
        btn1 = tk.Radiobutton(frameDaAplicacao, text='1 Player', font=('arial', 14), value=False, 
                       variable=self.modoJogo, bg='#dcdcdc')
        btn1.place(relx=0.27, rely=0.46)

        btn2 = tk.Radiobutton(frameDaAplicacao, text='2 Player', font=('arial', 14), value=True, 
                       variable=self.modoJogo, bg='#dcdcdc')
        btn2.place(relx=0.52, rely=0.46)

        #Botão para avançar
        btnSeguir = tk.Button(frameDaAplicacao, text='Seguir', bg='#dcdcdc', fg='#000000', font=('arial', 14, 'bold'), 
                  padx=16, pady=4, command=self.tela2)
        btnSeguir.place(relx=0.77, rely=0.73)

aplicacao = Aplicacao()