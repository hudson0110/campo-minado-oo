import random  # Importa a biblioteca random, que ajuda a escolher números aleatórios
from celula import Celula  # Importa a classe Celula de outro arquivo, que define cada quadrado no jogo

class Campo:
    def __init__(self, largura_tela, altura_tela, tamanho_celula, num_minas):
       
        self.largura_tela = largura_tela  # Define a largura da tela
        self.altura_tela = altura_tela  # Define a altura da tela
        self.tamanho_celula = tamanho_celula  # Define o tamanho de cada célula
        self.num_celulas_x = largura_tela // tamanho_celula  # Calcula quantas células cabem na largura
        self.num_celulas_y = altura_tela // tamanho_celula  # Calcula quantas células cabem na altura
        self.num_minas = num_minas  # Define quantas bombas haverá no jogo

        # Cria uma matriz (tabela) de células
        self.campo = [
            [Celula() for _ in range(self.num_celulas_x)]  # Cria uma linha de células
            for _ in range(self.num_celulas_y)  # Cria várias linhas para formar o tabuleiro
        ]

        # Inicializa o contador de minas colocadas
        self.minas_colocadas = 0  # Começamos com 0 minas no tabuleiro

    def criar_bombas(self, x_inicial, y_inicial):
        """
        Cria as bombas no campo, evitando a célula (x_inicial, y_inicial).

        
        Args:
            x_inicial (int): A posição x da célula clicada inicialmente.
            y_inicial (int): A posição y da célula clicada inicialmente.
        """
        self.minas_colocadas = 0  # Reinicia o contador de minas

        while self.minas_colocadas < self.num_minas:
            # Escolhe uma posição aleatória para a bomba
            x = random.randint(0, self.num_celulas_x - 1)
            y = random.randint(0, self.num_celulas_y - 1)

            # Evita colocar uma bomba na célula inicial clicada
            if (x, y) != (x_inicial, y_inicial) and not self.campo[y][x].bomba:
                self.campo[y][x].bomba = True  # Marca a célula como contendo uma bomba
                self.minas_colocadas += 1  # Aumenta o contador de minas

                # Atualiza o número de bombas ao redor da célula
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy  # Calcula a posição ao redor da bomba
                        # Verifica se a posição está dentro dos limites e se não é uma bomba
                        if 0 <= nx < self.num_celulas_x and 0 <= ny < self.num_celulas_y and not self.campo[ny][nx].bomba:
                            self.campo[ny][nx].numero += 1  # Aumenta o número de bombas ao redor

    def revelar_celula(self, x, y):
        """
        Revela a célula na posição (x, y) e revela células adjacentes se necessário.
        
        Args:
            x (int): A posição x da célula a ser revelada.
            y (int): A posição y da célula a ser revelada.
        """
        # Verifica se a célula já foi revelada
        if self.campo[y][x].revelada:
            return  # Se já foi revelada, não faz nada

        # Revela a célula
        self.campo[y][x].revelada = True

        # Se a célula tem número 0, revela todas as células adjacentes
        if self.campo[y][x].numero == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    # Verifica se a nova posição está dentro dos limites
                    if 0 <= nx < self.num_celulas_x and 0 <= ny < self.num_celulas_y:
                        self.revelar_celula(nx, ny)  # Revela as células adjacentes
