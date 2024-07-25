import pygame
from objeto_jogo import ObjetoJogo

class Bomba(ObjetoJogo):
    def __init__(self, x, y, tamanho):
        # Inicializa a posição e o tamanho da bomba
        super().__init__(x, y, tamanho)

    def desenhar(self, tela):
        # Desenha a bomba na tela
        cor = (255, 0, 0)  # Cor da bomba (vermelho)
        pygame.draw.rect(tela, cor, self.get_rect())  # Desenha o retângulo da bomba
        pygame.draw.rect(tela, (0, 0, 0), self.get_rect(), 1)  # Desenha o contorno da bomba (preto)
