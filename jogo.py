import pygame
from campo import Campo

class JogoCampoMinado:
    def __init__(self, largura_tela, altura_tela, tamanho_celula, num_minas):
        pygame.init()
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho_celula = tamanho_celula
        self.num_minas = num_minas
        self.campo = Campo(largura_tela, altura_tela, tamanho_celula, num_minas)
        self.tela = pygame.display.set_mode((largura_tela, altura_tela))
        pygame.display.set_caption("Campo Minado")
        self.fonte = pygame.font.SysFont(None, 36)
        self.executando = True
        self.vitoria = False
        self.derrota = False

    def __del__(self):
        pygame.quit()
        print("Jogo finalizado")

    def verificar_vitoria(self):
        for linha in self.campo.campo:
            for celula in linha:
                if not celula.get_bomba() and not celula.get_revelada():
                    return False
        return True

    def mostrar_mensagem(self, mensagem):
        self.tela.fill((150, 150, 150))
        texto = self.fonte.render(mensagem, True, (255, 255, 255))
        rect = texto.get_rect(center=(self.largura_tela // 2, self.altura_tela // 2))
        self.tela.blit(texto, rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def executar(self):
        while self.executando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.executando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = evento.pos
                    x //= self.tamanho_celula
                    y //= self.tamanho_celula
                    celula = self.campo.campo[y][x]
                    if evento.button == 1:
                        if not celula.get_marcada():
                            self.campo.revelar_celula(x, y)
                            if celula.get_bomba():
                                print("Você perdeu!")
                                self.derrota = True
                                self.executando = False
                    elif evento.button == 3:
                        celula.set_marcada(not celula.get_marcada())

            if self.verificar_vitoria():
                self.vitoria = True
                self.executando = False

            self.tela.fill((150, 150, 150))
            self.campo.desenhar(self.tela)
            pygame.display.flip()

        if self.vitoria:
            self.mostrar_mensagem("Você venceu!")
        elif self.derrota:
            self.mostrar_mensagem("Você perdeu!")