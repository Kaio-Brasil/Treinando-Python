import customtkinter as ctk
from screenDisplay import *
import adivinhe as ad # type: ignore
import mensagem as mens

class TelaDoGame(ScreenDisplay):
    def criarTela(self):
        self.telaPlayer1 = ctk.CTkToplevel()
        self.jogo = None

        dimencoes = self.dimencoesDaTela(self.telaPlayer1.winfo_screenwidth, self.telaPlayer1.winfo_screenheight)
        self.telaPlayer1.geometry('%dx%d+%d+%d'%(dimencoes[0], dimencoes[1], dimencoes[2], dimencoes[3]))
        self.telaPlayer1.geometry('400x500')
        self.telaPlayer1.title('App Adivinha')
        self.telaPlayer1.config(bg='#808080')
        self.telaPlayer1.resizable(width=False, height=False)
        self.telaPlayer1.transient(self.raiz)
        self.telaPlayer1.focus_force()
        self.telaPlayer1.grab_set()

        self.frameDaTela1()
        self.componentes()

    def frameDaTela1(self,
                     w: int = 360,
                     h: int = 450,
                     x: int = 0.05, 
                     y: int = 0.05,
                     bg: str = '#808080',
                     fg: str = '#dcdcdc',
                     bc: str = '#ffffff',
                     bwidth: int = 2,
                     corner: int = 20):
        self.frameTela1 = ctk.CTkFrame(master=self.telaPlayer1, width=w, height=h, corner_radius=corner,
                                       bg_color=bg, fg_color=fg, border_color=bc, border_width=bwidth)
        self.frameTela1.place(relx=x, rely=y)

    def componentes(self):
        self.labelComponent()
        self.entryComponent()
        self.buttonComponent()

    def labelComponent(self,
                     w: int = 300,
                     h: int = 40,
                     x: int = 0.25, 
                     y: int = 0.25,
                     txt: str ='Diga seu palpite \nde 0 a 10?',
                     font = ('<arial>', 24, 'bold'),
                     justify: str = 'center'):
        
        lbl = ctk.CTkLabel(master=self.frameTela1, text=txt, font=font, justify=justify)
        lbl.place(relx=x, rely=y)

    def entryComponent(self,
                     w: int = 220,
                     h: int = 40,
                     x: int = 0.2, 
                     y: int = 0.45,
                     font = ('<arial>', 16),
                     bg: str = '#808080',
                     fg: str = '#dcdcdc',
                     bc: str = '#808080',
                     bcf: str = '#111111',
                     bwidth: int = 2,
                     corner: int = 20):
        
        def chamarFuncao(event):
            self.iniciar()
    
        self.entryPalpite = ctk.CTkEntry(master=self.frameTela1, width=w, height=h, font=font, border_color=bc)
        self.entryPalpite.place(relx=x, rely=y)
        self.entryPalpite.bind('<Return>', chamarFuncao)

    def buttonComponent(self,
                     w: int = 100,
                     h: int = 38,
                     x: int = 0.38, 
                     y: int = 0.62,
                     txt: str = 'Palpite',
                     txtcolor: str = '#ffffff',
                     font = ('<arial>', 16, 'bold'),
                     bg: str = '#808080',
                     fg: str = '#dcdcdc',
                     bc: str = '#808080',
                     bcf: str = '#111111',
                     bwidth: int = 1,
                     corner: int = 20):
    
        btn = ctk.CTkButton(self.frameTela1, text=txt,  width=w, height=h, text_color=txtcolor, font=font, 
                            border_width=bwidth, border_color=bcf, command=self.iniciar)
        btn.place(relx=x, rely=y)

    def iniciar(self):
        self.jogo = ad.Adivinhe()

        number = self.entryPalpite.get()
        self.entryPalpite.delete(0, 'end')
        self.jogo.jogarModInterFace(number)

    def fechar(self):
        self.tela1Player.destroy()
        self.tela1Player = None

    def avisar(ttl, msn):
        mensagem = mens.Mensagem()
        mensagem.aletar(ttl, msn)
