# Importa o módulo pygame para poder usar suas funções
import pygame
# Importa a classe Campo do arquivo campo.py para usar no jogo
from campo import Campo

# Define a classe JogoCampoMinado, que vai gerenciar o jogo
class JogoCampoMinado:
    # O método __init__ é chamado quando criamos um novo objeto dessa classe
    def __init__(self, largura_tela, altura_tela, tamanho_celula, num_minas):
        # Inicializa o pygame para usar suas funcionalidades
        pygame.init()
        # Define a largura da tela do jogo
        self.largura_tela = largura_tela
        # Define a altura da tela do jogo
        self.altura_tela = altura_tela
        # Define o tamanho de cada célula do campo minado
        self.tamanho_celula = tamanho_celula
        # Define o número de minas no jogo
        self.num_minas = num_minas
        # Cria um objeto Campo que representa o campo minado do jogo
        self.campo = Campo(largura_tela, altura_tela, tamanho_celula, num_minas)
        # Cria a tela onde o jogo será exibido, com a largura e altura definidas
        self.tela = pygame.display.set_mode((largura_tela, altura_tela))
        # Define o título da janela do jogo
        pygame.display.set_caption("Campo Minado")
        # Cria um objeto fonte para desenhar textos na tela
        self.fonte = pygame.font.SysFont(None, 36)
        # Define uma variável que indica se o jogo está rodando
        self.executando = True

    # O método __del__ é chamado quando o objeto é destruído
    def __del__(self):
        # Finaliza o pygame e fecha o jogo
        pygame.quit()
        # Imprime uma mensagem dizendo que o jogo foi finalizado
        print("Jogo finalizado")

    # Define o método executar, que é responsável por rodar o jogo
    def executar(self):
        # Enquanto o jogo estiver rodando
        while self.executando:
            # Pega todos os eventos que aconteceram (como cliques do mouse)
            for evento in pygame.event.get():
                # Se o evento for fechar a janela
                if evento.type == pygame.QUIT:
                    # Para o jogo
                    self.executando = False
                # Se o evento for um clique do mouse
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    # Pega a posição do clique do mouse
                    x, y = evento.pos
                    # Converte a posição do clique para a célula correspondente
                    x //= self.tamanho_celula
                    y //= self.tamanho_celula
                    # Pega a célula clicada
                    celula = self.campo.campo[y][x]
                    # Se o botão do mouse clicado for o esquerdo (1)
                    if evento.button == 1:
                        # Se a célula não estiver marcada com uma bandeira
                        if not celula.get_marcada():
                            # Revela a célula
                            self.campo.revelar_celula(x, y)
                            # Se a célula tem uma bomba
                            if celula.get_bomba():
                                # Imprime uma mensagem de perda
                                print("Você perdeu!")
                                # Para o jogo
                                self.executando = False
                    # Se o botão do mouse clicado for o direito (3)
                    elif evento.button == 3:
                        # Marca ou desmarca a célula com uma bandeira
                        celula.set_marcada(not celula.get_marcada())

            # Limpa a tela com a cor cinza escuro
            self.tela.fill((150, 150, 150))
            # Desenha o campo minado na tela
            self.campo.desenhar(self.tela)
            # Atualiza a tela para mostrar as mudanças
            pygame.display.flip()
