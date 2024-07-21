import pygame  # Importa a biblioteca pygame, que ajuda a criar jogos e gráficos
from campo import Campo  # Importa a classe Campo de outro arquivo que define o tabuleiro do jogo

# Define as cores que usaremos no jogo
PRETO = (0, 0, 0)  # Preto
BRANCO = (255, 255, 255)  # Branco
CINZA_CLARO = (200, 200, 200)  # Cinza claro
CINZA_ESCURO = (150, 150, 150)  # Cinza escuro
VERMELHO = (255, 0, 0)  # Vermelho

# Define a classe do jogo
class JogoCampoMinado:
    def __init__(self, largura_tela, altura_tela, tamanho_celula, num_minass):
        # Inicializa o jogo com o tamanho da tela e o número de minas
        self.campo = Campo(largura_tela, altura_tela, tamanho_celula, num_minass)
        self.executando = True  # Define que o jogo está rodando
        self.tamanho_celula = tamanho_celula  # Tamanho de cada quadrado na tela
        self.bombas_geradas = False  # Variável para verificar se as bombas já foram geradas

        # Configura a tela onde o jogo será exibido
        self.tela = pygame.display.set_mode((largura_tela, altura_tela))
        pygame.display.set_caption("Campo Minado")  # Define o título da janela do jogo

        # Configura a fonte para escrever texto na tela
        self.fonte = pygame.font.SysFont(None, 36)

    def desenhar_campo(self):
        # Esta função desenha o campo do jogo na tela

        # Percorre todas as linhas e colunas do campo
        for y in range(self.campo.num_celulas_y):
            for x in range(self.campo.num_celulas_x):
                # Define a posição e o tamanho do quadrado (célula) que será desenhado
                rect = pygame.Rect(x * self.tamanho_celula, y * self.tamanho_celula, self.tamanho_celula, self.tamanho_celula)
                celula = self.campo.campo[y][x]  # Pega a célula atual do campo
                
                if celula.revelada:  # Se a célula foi revelada
                    if celula.bomba:  # Se a célula tem uma bomba
                        pygame.draw.rect(self.tela, VERMELHO, rect)  # Desenha a célula em vermelho
                    else:
                        pygame.draw.rect(self.tela, BRANCO, rect)  # Desenha a célula em branco
                        if celula.numero > 0:  # Se a célula tem números
                            texto = self.fonte.render(str(celula.numero), True, PRETO)  # Cria o texto com o número
                            self.tela.blit(texto, rect.move(10, 5))  # Desenha o texto na célula
                else:  # Se a célula não foi revelada
                    pygame.draw.rect(self.tela, CINZA_CLARO, rect)  # Desenha a célula em cinza claro
                    if celula.marcada:  # Se a célula está marcada com uma bandeira
                        texto = self.fonte.render("|>", True, PRETO)  # Cria o texto com a bandeira
                        self.tela.blit(texto, rect.move(10, 5))  # Desenha a bandeira na célula
                pygame.draw.rect(self.tela, PRETO, rect, 1)  # Desenha a borda preta da célula

    def gerar_bombas(self, x_inicial, y_inicial):
        """Gera bombas no campo, evitando a célula inicial onde o jogador clicou."""
        self.campo.criar_bombas(x_inicial, y_inicial)
        self.bombas_geradas = True

    def interagir(self):
        # Esta função lida com a interação do jogador (cliques do mouse)
        while self.executando:  # Enquanto o jogo estiver rodando
            for evento in pygame.event.get():  # Pega todos os eventos (como cliques) que aconteceram
                if evento.type == pygame.QUIT:  # Se o evento for fechar a janela
                    self.executando = False  # Para o jogo
                elif evento.type == pygame.MOUSEBUTTONDOWN:  # Se o evento for um clique do mouse
                    x, y = evento.pos  # Pega a posição do clique
                    x //= self.tamanho_celula  # Converte a posição do clique para a célula correspondente
                    y //= self.tamanho_celula
                    celula = self.campo.campo[y][x]  # Pega a célula clicada
                    if evento.button == 1:  # Se o botão do mouse clicado for o esquerdo
                        if not celula.marcada:  # Se a célula não estiver marcada com uma bandeira
                            if not self.bombas_geradas:  # Se as bombas ainda não foram geradas
                                self.gerar_bombas(x, y)  # Gera as bombas
                            self.campo.revelar_celula(x, y)  # Revela a célula
                            if celula.bomba:  # Se a célula tem uma bomba
                                print("Você perdeu!")  # Mostra mensagem de perda
                                self.executando = False  # Para o jogo
                    elif evento.button == 3:  # Se o botão do mouse clicado for o direito
                        celula.marcada = not celula.marcada  # Marca ou desmarca a célula com uma bandeira

            self.tela.fill(CINZA_ESCURO)  # Limpa a tela com a cor cinza escuro
            self.desenhar_campo()  # Desenha o campo na tela
            pygame.display.flip()  # Atualiza a tela para mostrar as mudanças

        pygame.quit()  # Fecha o pygame quando o jogo termina
