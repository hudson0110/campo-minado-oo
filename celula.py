import pygame
from objeto_jogo import ObjetoJogo

class Celula(ObjetoJogo):
    def __init__(self, x, y, tamanho):
        # Posição, tamanho e estado da célula
        super().__init__(x, y, tamanho)
        self._bomba = False
        self._revelada = False
        self._marcada = False
        self._numero = 0

    # Gets
    def get_bomba(self):
        return self._bomba   # Retorna se a célula contém uma bomba

    def get_revelada(self):
        return self._revelada  # Retorna se a célula está revelada

    def get_marcada(self):
        return self._marcada  # Retorna se a célula está marcada com uma bandeira

    def get_numero(self):
        return self._numero  # Retorna o número de bombas vizinhas

    # Sets
    def set_bomba(self, bomba):
        self._bomba = bomba  # Define se a célula tem uma bomba

    def set_revelada(self, revelada):
        self._revelada = revelada  # Define se a célula está revelada

    def set_marcada(self, marcada):
        self._marcada = marcada  # Define se a célula está marcada com uma bandeira

    def set_numero(self, numero):
        self._numero = numero  # Define o número de bombas vizinhas

    def desenhar(self, tela):
        if self._revelada:  # Desenha a célula na tela
            cor = (200, 200, 200)  # Célula revelada (branco)
            pygame.draw.rect(tela, cor, self.get_rect())
            if self._numero > 0:
                fonte = pygame.font.SysFont(None, 36)
                texto = fonte.render(str(self._numero), True, (0, 0, 0))  # Desenha o número de bombas adjacentes
                tela.blit(texto, (self.get_x() * self.get_tamanho() + 10, self.get_y() * self.get_tamanho() + 5))
        else:
            cor = (0, 0, 0)  # Cor da célula não revelada (cinza claro)
            pygame.draw.rect(tela, cor, self.get_rect())
            if self._marcada:
                fonte = pygame.font.SysFont(None, 36)
                texto = fonte.render("|^", True, (255, 255, 255))  # Desenha a bandeira na célula marcada
                tela.blit(texto, (self.get_x() * self.get_tamanho() + 10, self.get_y() * self.get_tamanho() + 5))
        pygame.draw.rect(tela, (255, 255, 255), self.get_rect(), 1)  # Desenha o contorno da célula (branco)
