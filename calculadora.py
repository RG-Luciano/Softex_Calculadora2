def calculadora(operador, num1, num2):
    if operador == 1:
        print("O resultado é:", num1+num2)
    elif operador == 2:
        print("O resultado é:", num1-num2)
    elif operador == 3:
        print("O resultado é:", num1*num2)
    elif operador == 4:
        print("O Resultadoé:", num1/num2)

operador = 1

while operador:
    print("\nEscolha uma opção: ")
    print("1: Para soma")
    print("2: Para subtração")
    print("3: Para multiplicação")
    print("4: Para divisão")
    print("0: Para sair!!")
    operador = int(input('Operador: '))
    if operador == 0:
        print("Calculadora encerrada!!")
        exit()
    elif 1 <= operador <= 4:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        calculadora(operador, num1, num2)
    else:
        print("\nOperação Invalida!!")