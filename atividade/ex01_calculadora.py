import os
os.system("cls")

print("=" *35)
print("Calculadora para os Atendentes. ")
print("=" *35)
print()
print("Insira os cálculos e gere os resultados")

n1 = int(input("Digite 1ª Número: "))
n2 = int(input("Digite 2ª Número: "))
operacao = input("Digite a Operação ( | + | - | * | / | ): ")

match operacao:
    case "+":
        resultado = n1 + n2
        print(f"O Resultado é: {resultado}")
    case "-":
        resultado = n1 - n2
        print(f"O Resultado é: {resultado}")
    case "*":
        resultado = n1 * n2
        print(f"O Resultado é: {resultado}")
    case "/":
        if n2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            resultado = n1 / n2
            print(f"O Resultado é: {resultado}")
    case _:
        print("Operação inválida! Use apenas +, -, * ou /.")