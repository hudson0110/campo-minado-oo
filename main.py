import pygame
from jogo import JogoCampoMinado

# Configurações do jogo

LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_CELULA = 40
NUM_MINAS = 40


def main():
    pygame.init()
    jogo = JogoCampoMinado(LARGURA_TELA, ALTURA_TELA, TAMANHO_CELULA, NUM_MINAS)
    jogo.interagir()
    pygame.quit()

if __name__ == "__main__":
    main()