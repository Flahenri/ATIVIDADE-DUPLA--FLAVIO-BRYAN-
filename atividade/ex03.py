import os
os.system("cls")

numeros = []
quantidade_numerica = 10

for i in range(quantidade_numerica):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)

maiores_que_10 = sum(1 for num in numeros if num > 10)
print(f"Soma de todos os elementos: {soma}")
print(f"Quantidade de números maiores que 10: {maiores_que_10}")
