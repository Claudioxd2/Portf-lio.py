import math

def calculadora_basica():
    """Executa operações básicas de uma calculadora."""
    print("\n--- Calculadora Básica ---")
    while True:
        print("\nSelecione a operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Voltar ao menu principal")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            break
        elif escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print("Resultado:", num1 + num2)
                elif escolha == '2':
                    print("Resultado:", num1 - num2)
                elif escolha == '3':
                    print("Resultado:", num1 * num2)
                elif escolha == '4':
                    if num2 == 0:
                        print("Erro! Divisão por zero não é permitida.")
                    else:
                        print("Resultado:", num1 / num2)
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def calculadora_cientifica():
    """Executa operações científicas de uma calculadora."""
    print("\n--- Calculadora Científica ---")
    while True:
        print("\nSelecione a operação:")
        print("1. Raiz Quadrada (sqrt)")
        print("2. Potenciação (^)")
        print("3. Logaritmo Natural (ln)")
        print("4. Logaritmo Base 10 (log10)")
        print("5. Seno (sin)")
        print("6. Cosseno (cos)")
        print("7. Tangente (tan)")
        print("8. Voltar ao menu principal")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '8':
            break
        elif escolha in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num = float(input("Digite o número: "))

                if escolha == '1':
                    if num >= 0:
                        print("Resultado:", math.sqrt(num))
                    else:
                        print("Erro! Não é possível calcular a raiz quadrada de um número negativo.")
                elif escolha == '2':
                    expoente = float(input("Digite o expoente: "))
                    print("Resultado:", math.pow(num, expoente))
                elif escolha == '3':
                    if num > 0:
                        print("Resultado:", math.log(num))
                    else:
                        print("Erro! O logaritmo natural só é definido para números positivos.")
                elif escolha == '4':
                    if num > 0:
                        print("Resultado:", math.log10(num))
                    else:
                        print("Erro! O logaritmo base 10 só é definido para números positivos.")
                elif escolha == '5':
                    print("Resultado:", math.sin(math.radians(num))) # Converte para radianos
                elif escolha == '6':
                    print("Resultado:", math.cos(math.radians(num))) # Converte para radianos
                elif escolha == '7':
                    print("Resultado:", math.tan(math.radians(num))) # Converte para radianos
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        else:
            print("Escolha inválida. Por favor, tente novamente.")

def menu_principal():
    """Exibe o menu principal da calculadora."""
    while True:
        print("\n--- Calculadora ---")
        print("Selecione o tipo de calculadora:")
        print("1. Básica")
        print("2. Científica")
        print("3. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            calculadora_basica()
        elif escolha == '2':
            calculadora_cientifica()
        elif escolha == '3':
            print("Saindo da calculadora. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()
