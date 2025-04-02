def exibir_tabuleiro(tabuleiro):
    
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro, jogador):
    
    # Verifica linhas
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True

    # Verifica colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogar_jogo_da_velha():
    
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha = int(input("Digite o número da linha (0, 1 ou 2): "))
            coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

            if not (0 <= linha <= 2 and 0 <= coluna <= 2):
                raise ValueError("Linha ou coluna fora do intervalo válido.")

            if tabuleiro[linha][coluna] != " ":
                raise ValueError("Casa já ocupada. Tente novamente.")

            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1

            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"

        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

    else:
        exibir_tabuleiro(tabuleiro)
        print("Empate!")

jogar_jogo_da_velha()