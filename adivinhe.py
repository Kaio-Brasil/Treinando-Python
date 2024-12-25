from random import randint
from re import compile, search

#O jogo advinhe pode ser jogado no modo prompt ou pela interface gráfica tkinter
class Adivinhe:
    def __init__(self):
        self.valorAleatorio = 0
        self.guess = 0
        self.quantPalpite = 0

    def verificarDigito(self, number):
        pattern = compile('[0-9]')
        
        if search(pattern, number):
            return number
        return '0'

    def getPaltipe(self):
        return self.quantPalpite
    
    def gerarNumeroAleatorio(self):
        return randint(1, 10)
    
    def zerarQuantidadePaltipe(self):
        self.quantPalpite = 0

    def contarPalpite(self):
        self.quantPalpite = self.quantPalpite + 1
           
    def mostarMensagem(msn):
        print(msn)
    
    #modo -> Qual estilo vai ser jogado interface gráfica ou prompt
    def jogarModTerminal(self):
        self.zerarQuantidadePaltipe()
        self.valorAleatorio = self.gerarNumeroAleatorio()

        number = input('Diga seu palpite entre 1 a 10?\n')

        self.guess = int(self.verificarDigito(number))

        if self.guess == 0:
            self.mostarMensagem('Valor digitado invalido!')
            self.jogarModTerminal()

        while True:
            self.contarPalpite()
    
            if self.guess < self.valorAleatorio:
                self.guess = int(input('Chute um numero maior!\n'))
            elif self.guess > self.valorAleatorio:
                self.guess = int(input('Chute um numero menor!\n'))
            elif self.guess == self.valorAleatorio:
                self.mostarMensagem('Voce acertou, parabens!!!\nQuantidade de palpites '+str(self.quantPalpite)+'\n')
            return self.quantPalpite

    def jogarModInterFace(self, number):
        self.zerarQuantidadePaltipe()
        self.valorAleatorio = self.gerarNumeroAleatorio()

        self.guess = int(self.verificarDigito(number))

        if self.guess == 0:
            return 0
        
        if self.guess < self.valorAleatorio:
            self.guess = int(input('Chute um numero maior!\n'))
        elif self.guess > self.valorAleatorio:
            self.guess = int(input('Chute um numero menor!\n'))
        elif self.guess == self.valorAleatorio:
            self.mostarMensagem('Voce acertou, parabens!!!\nQuantidade de palpites '+str(self.quantPalpite)+'\n')
        return self.quantPalpite

