# main.py

from jogo import JogoCampoMinado

largura_tela = 400
altura_tela = 400
tamanho_celula = 40
num_minas = 12

def main():
    jogo = JogoCampoMinado(largura_tela, altura_tela, tamanho_celula, num_minas)
    jogo.campo.criar_bombas(x_inicial=0, y_inicial=0)
    jogo.executar()

if __name__ == "__main__":
    main()
