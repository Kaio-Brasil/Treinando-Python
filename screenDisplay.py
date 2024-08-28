class ScreenDisplay:
    def dimencoesDeTela(self, screenwidth, screenheight):
        LARGURA = 800
        ALTURA = 500
        LARGURA_SCREEN = screenwidth()
        ALTURA_SCREEN = screenheight()
        POSX = LARGURA_SCREEN/2 - LARGURA/2
        POSY = ALTURA_SCREEN/2 - ALTURA/2

        return LARGURA, ALTURA, POSX, POSY
    