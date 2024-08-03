import jogoAdivinhe
import player
import re

class Jogo:
    def __init__(self):
        self.jogo = None
        self.quantidadeJogadores = 0
        self.quantidadePartidas = 0
        self.palpites = 0
        self.jogadores = []

    def verificarQuantidadeDefinida(self, quant, min, max):
        if quant >= min and quant <= max:
            return True
        return False
    
    def verificarPadrao(self, numero):
        pattern = re.compile('[0-9]')
        
        if re.search(pattern, numero):
            return numero
        return '0'
    
    def somarPalpites(self, resultado):
        self.palpites = self.palpites + resultado

    def verificarVencedor(self):
        vencedor = ''
        copia = self.jogadores.copy()
    
        for i in range(len(self.jogadores) - 1):
            for j in range(self.quantidadePartidas):
                if copia[i].palpite > copia[i+1].palpite:
                    vencedor = copia[i+1].nome
                elif copia[i].palpite < copia[i+1].palpite:
                    vencedor = copia[i].nome
                else:
                    vencedor = 'Empate'
        
        if not vencedor.__eq__('Empate'):
            print('Com menos palpite o jogador {} foi o venceu!\n'.format(vencedor.upper()))
        else:
            print('O jogo foi empatado!')

    def resultadoDosJogadores(self):
        for ver in self.jogadores:
            print('Nome: {}, palpite: {}'.format(ver.nome, ver.palpite))
    
    def criarJogadores(self):
        for n in range(self.quantidadeJogadores):
            nome = input('Digite o nome do player{}?\n'.format(n+1))
            jogador = player.Player(nome, 0)
            self.jogadores.append(jogador)

    def iniciarCompeticao(self):

        for jogadorDaVez in self.jogadores:
            vezes = 0
            self.palpites = 0
            
            print('\nO jogador da vez: {}'.format(jogadorDaVez.nome))

            while vezes < self.quantidadePartidas:
                self.jogo.jogar()
                self.somarPalpites(self.jogo.getPaltipe())
                jogadorDaVez.palpite = self.palpites
                vezes = vezes + 1

    def novoJogo(self):
        queroJogar = input('\nDeseja jogar novamente? S/N\n')

        if queroJogar.lower() == 's':
            self.iniciar()
        else:
            print('Ate logo!')

    def iniciar(self):
        self.jogo = jogoAdivinhe.JogoAdivinhe()
        jogar = input('Digite 1 para jogar sozinho ou 2 para jogar com adversario(s)?\n')
        opcoes = self.verificarPadrao(jogar)

        match opcoes:
            case '1':
                self.jogo.jogar()
            case '2':
                resposta = input('Digite a quantidade de jogadores? (2 ate 5)\n')
                self.quantidadeJogadores = int(self.verificarPadrao(resposta))

                if self.verificarQuantidadeDefinida(self.quantidadeJogadores, 2, 5):
                    self.criarJogadores()
                else:
                    print('Valor digitado invalido!')
                    print('Deve ser um numero e esta entre 2 e 5!')
                    self.novoJogo()

                partidas = input('Digite a quantidade de partidas que vai jogar? (1 ate 9)\n')
                self.quantidadePartidas = int(self.verificarPadrao(partidas))
            
                if self.verificarQuantidadeDefinida(self.quantidadePartidas, 1, 9):
                    self.iniciarCompeticao()
                    self.verificarVencedor()
                    self.resultadoDosJogadores()
                else:
                    print('Numero de partidas nao atende aos requisitos!')

            case _:
                print('Voce nao escolheu nenhuma opcao valida!\n')
                
        self.jogadores = []
        self.novoJogo()

jogo = Jogo()
jogo.iniciar()
