from random import randint
from re import compile, search

class JogoAdivinhe:
    def __init__(self):
        self.valorAleatorio = 0
        self.palpite = 0
        self.quantPalpite = 0

    def verificarPadrao(self, numero):
        pattern = compile('[0-9]')
        
        if search(pattern, numero):
            return numero
        return '0'

    def getPaltipe(self):
        return self.quantPalpite
    
    def gerarNumeroAleatorio(self):
        return randint(1, 10)
    
    def zerarQuantidadePaltipe(self):
        self.quantPalpite = 0

    def contarPalpite(self):
        self.quantPalpite = self.quantPalpite + 1
    
    def jogar(self):
        self.zerarQuantidadePaltipe()
        self.valorAleatorio = self.gerarNumeroAleatorio()
        numero = input('Diga seu palpite entre 1 a 10?\n')
        self.palpite = int(self.verificarPadrao(numero))

        if self.palpite == 0:
            print('Valor digitado invalido!')
            self.jogar()

        while True:
            self.contarPalpite()
    
            if self.palpite < self.valorAleatorio:
                self.palpite = int(input('Chute um numero maior!\n'))
            elif self.palpite > self.valorAleatorio:
                self.palpite = int(input('Chute um numero menor!\n'))
            elif self.palpite == self.valorAleatorio:
                print('Voce acertou, parabens!!!\nQuantidade de palpites '+str(self.quantPalpite)+'\n')
                return self.quantPalpite
