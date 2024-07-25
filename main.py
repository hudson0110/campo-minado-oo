from jogo import JogoCampoMinado

# Configurações do jogo
largura_tela = 400
altura_tela = 400
tamanho_celula = 40
num_minas = 15

def main():
    # Instancia o objeto jogo
    jogo = JogoCampoMinado(largura_tela, altura_tela, tamanho_celula, num_minas)
    
    # Inicia o jogo criando as bombas
    jogo.campo.criar_bombas(x_inicial=0, y_inicial=0)
    
    # Executa o loop principal
    jogo.executar()

if __name__ == "__main__":
    # Executa a função principal se este arquivo for executado diretamente
    main()
