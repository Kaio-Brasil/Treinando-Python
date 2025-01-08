import tkinter as tk
import customtkinter as ctk # type: ignore
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
        self.components()
        self.raiz.mainloop()

    def tela(self):
        dimencoes = self.dimencoesDaTelaPrincipal(self.raiz.winfo_screenwidth, self.raiz.winfo_screenheight) #Chamada da class screenDisplay
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

    def frameDaTelaPrincipal(self, 
                             w: int = 750,
                             h: int = 450,
                             x: float = 0.03, 
                             y: float = 0.05,
                             bg: str = '#808080',
                             fg: str = '#dcdcdc',
                             bc: str = '#ffffff',
                             bwidth: int = 2,
                             corner: int = 20):
        self.framePrincipal = ctk.CTkFrame(master=self.raiz, width=w, height=h, corner_radius=corner,
                                       bg_color=bg, fg_color=fg, border_color=bc, border_width=bwidth)
        self.framePrincipal.place(relx=x, rely=y)

    def components(self):
        self.modoJogo = tk.BooleanVar()

        self.labelTitleComponent()
        self.frameDaAplicacaoComponent()
        self.labelPerguntaComponent()
        self.radioButton1Component()
        self.radioButton2Component()
        self.buttonComponent()
    
    def labelTitleComponent(self,
                             w: int = 300,
                             h: int = 32,
                             x: float = 0.35, 
                             y: float = 0.08,
                             txt: str ='Jogo do Adivinha',
                             font = ('<verdana>', 30, 'bold'),
                             txtc: str = '#ff4500',
                             fg: str = '#dcdcdc', 
                             justify: str = 'center'):
        lblTitulo = ctk.CTkLabel(master=self.framePrincipal, text=txt, justify=justify, fg_color=fg, 
                                 text_color=txtc, font=font)
        lblTitulo.place(relx=x, rely=y)

    def frameDaAplicacaoComponent(self, 
                             w: int = 700,
                             h: int = 320,
                             x: float = 0.03, 
                             y: float = 0.23,
                             bg: str = '#dcdcdc',
                             fg: str = '#dcdcdc',
                             bc: str = '#111111',
                             bwidth: int = 2,
                             corner: int = 20):
        self.frameDaAplicacao = ctk.CTkFrame(master=self.framePrincipal, width=w, height=h, bg_color=bg, fg_color=fg,
                                        corner_radius=corner, border_color=bc, border_width=bwidth)
        self.frameDaAplicacao.place(relx=x, rely=y)

    def labelPerguntaComponent(self,
                             w: int = 300,
                             h: int = 40,
                             x: float = 0.23, 
                             y: float = 0.22,
                             txt: str ='Escola o modo de jogo que deseja jogar?',
                             font = ('<arial>', 20),
                             txtc: str = '#ff4500',
                             fg: str = '#000000', 
                             justify: str = 'center'):
        lblPerguta = ctk.CTkLabel(master=self.frameDaAplicacao, text=txt, justify=justify, font=font)
        lblPerguta.place(relx=x, rely=y)

    def radioButton1Component(self,
                             w: int = 30,
                             h: int = 30,
                             x: float = 0.34,
                             y: float = 0.46,
                             rb_width: int = 20, 
                             rb_height: int = 20,
                             b_color: str = '#111111', 
                             txt: str = '1 Player',
                             font = ('<arial>', 16, 'bold'),
                             txtc: str = '#ff4500',
                             fg: str = '#4682bb', 
                             vall: bool = False):
        self.btn1 = ctk.CTkRadioButton(master=self.frameDaAplicacao, width=w, height=h, radiobutton_width=rb_width, 
                                       radiobutton_height=rb_height, text=txt, font=font, value=vall, fg_color=fg, 
                                       border_color=b_color, variable=self.modoJogo)
        self.btn1.place(relx=x, rely=y)

    def radioButton2Component(self,
                         w: int = 30,
                         h: int = 30,
                         x: float = 0.54,
                         y: float = 0.46,
                         rb_width: int = 20, 
                         rb_height: int = 20,
                         b_color: str = '#111111', 
                         txt: str = '2 Player',
                         font = ('<arial>', 16, 'bold'),
                         txtc: str = '#ff4500',
                         fg: str = '#4682bb', 
                         vall: bool = True):
            self.btn2 = ctk.CTkRadioButton(master=self.frameDaAplicacao, width=w, height=h, radiobutton_width=rb_width, 
                                       radiobutton_height=rb_height, text=txt, font=font, value=vall, fg_color=fg, 
                                       border_color=b_color, variable=self.modoJogo)
            self.btn2.place(relx=x, rely=y)

    def buttonComponent(self,
                         w: int = 100,
                         h: int = 40,
                         x: float = 0.70,
                         y: float = 0.70,
                         b_color: str = '#111111', 
                         txt: str = 'Seguir',
                         font = ('<arial>', 16, 'bold'),
                         txtc: str = '#ffffff',
                         fg: str = '#000000'):
        btnSeguir = ctk.CTkButton(master=self.frameDaAplicacao, text=txt, text_color=txtc, width=w, height=h,
                                   font=font, command=self.tela2)
        btnSeguir.place(relx=x, rely=y)


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