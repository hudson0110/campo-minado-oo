# campo.py

import random
from celula import Celula
from bomba import Bomba

class Campo:
    def __init__(self, largura_tela, altura_tela, tamanho_celula, num_minas):
        # Inicializa o jogo com as dimensões da tela, tamanho das células e número de minas
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho_celula = tamanho_celula
        self.num_celulas_x = largura_tela // tamanho_celula
        self.num_celulas_y = altura_tela // tamanho_celula
        self.num_minas = num_minas
        self.campo = [[Celula(x, y, tamanho_celula) for x in range(self.num_celulas_x)] for y in range(self.num_celulas_y)]
        self.minas_colocadas = 0

    def criar_bombas(self, x_inicial, y_inicial):
        # Coloca as bombas no campo depois do primeiro clique
        self.minas_colocadas = 0
        while self.minas_colocadas < self.num_minas:
            x = random.randint(0, self.num_celulas_x - 1)
            y = random.randint(0, self.num_celulas_y - 1)
            if (x, y) != (x_inicial, y_inicial) and not self.campo[y][x].get_bomba():
                self.campo[y][x].set_bomba(True)
                self.minas_colocadas += 1
                # Incrementa o número das células vizinhas à bomba
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.num_celulas_x and 0 <= ny < self.num_celulas_y and not self.campo[ny][nx].get_bomba():
                            self.campo[ny][nx].set_numero(self.campo[ny][nx].get_numero() + 1)

    def revelar_celula(self, x, y):
        # Revela a célula selecionada e, se for um espaço vazio, revela as células vizinhas 
        if self.campo[y][x].get_revelada():
            return
        self.campo[y][x].set_revelada(True)
        if self.campo[y][x].get_numero() == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.num_celulas_x and 0 <= ny < self.num_celulas_y:
                        self.revelar_celula(nx, ny)

    def revelar_todas_as_bombas(self):
        # Revela todas as bombas
        for linha in self.campo:
            for celula in linha:
                if celula.get_bomba():
                    celula.set_revelada(True)

    def desenhar(self, tela):
        # Desenha todas as células do jogo
        for linha in self.campo:
            for celula in linha:
                celula.desenhar(tela)
