
import pygame

class ObjetoJogo:

    def __init__(self, x, y, tamanho):
        self._x = x  # Posições X do quadrado (como um número para onde ele está na tela)
        self._y = y  # Posições Y do quadrado (como um número para onde ele está na tela)
        self._tamanho = tamanho  
        # Cria um retângulo (quadrado) que vai desenhar na tela. 
        self._rect = pygame.Rect(x * tamanho, y * tamanho, tamanho, tamanho)

    # Método para pegar a posição X do quadrado
    def get_x(self):
        return self._x

    # Método para pegar a posição Y do quadrado
    def get_y(self):
        return self._y

    # Método para pegar o tamanho do quadrado
    def get_tamanho(self):
        return self._tamanho

    # Método para pegar o retângulo que representa o quadrado na tela
    def get_rect(self):
        return self._rect

    # Método para definir (mudar) a posição X do quadrado
    def set_x(self, x):
        self._x = x
        # Atualiza a posição do retângulo na tela para refletir a nova posição X
        self._rect.x = x * self._tamanho

    # Método para definir (mudar) a posição Y do quadrado
    def set_y(self, y):
        self._y = y
        # Atualiza a posição do retângulo na tela para refletir a nova posição Y
        self._rect.y = y * self._tamanho