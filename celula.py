# celula.py
import pygame

from objeto_jogo import ObjetoJogo

class Celula(ObjetoJogo):
    def __init__(self, x, y, tamanho):
        super().__init__(x, y, tamanho)
        self._bomba = False
        self._revelada = False
        self._marcada = False
        self._numero = 0

    # Métodos get
    def get_bomba(self):
        return self._bomba

    def get_revelada(self):
        return self._revelada

    def get_marcada(self):
        return self._marcada

    def get_numero(self):
        return self._numero

    # Métodos set
    def set_bomba(self, bomba):
        self._bomba = bomba

    def set_revelada(self, revelada):
        self._revelada = revelada

    def set_marcada(self, marcada):
        self._marcada = marcada

    def set_numero(self, numero):
        self._numero = numero

    def desenhar(self, tela):
        if self._revelada:
            cor = (255, 255, 255)  # Branco
            pygame.draw.rect(tela, cor, self.get_rect())
            if self._numero > 0:
                fonte = pygame.font.SysFont(None, 36)
                texto = fonte.render(str(self._numero), True, (0, 0, 0))
                tela.blit(texto, (self.get_x() * self.get_tamanho() + 10, self.get_y() * self.get_tamanho() + 5))
        else:
            cor = (200, 200, 200)  # Cinza claro
            pygame.draw.rect(tela, cor, self.get_rect())
            if self._marcada:
                fonte = pygame.font.SysFont(None, 36)
                texto = fonte.render("|>", True, (0, 0, 0))
                tela.blit(texto, (self.get_x() * self.get_tamanho() + 10, self.get_y() * self.get_tamanho() + 5))
        pygame.draw.rect(tela, (0, 0, 0), self.get_rect(), 1)  # Contorno preto
