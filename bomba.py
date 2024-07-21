# bomba.py

import pygame
# bomba.py

from objeto_jogo import ObjetoJogo

class Bomba(ObjetoJogo):
    def __init__(self, x, y, tamanho):
        super().__init__(x, y, tamanho)

    def desenhar(self, tela):
        cor = (255, 0, 0)  # Vermelho
        pygame.draw.rect(tela, cor, self.get_rect())
        pygame.draw.rect(tela, (0, 0, 0), self.get_rect(), 1)  # Contorno preto
