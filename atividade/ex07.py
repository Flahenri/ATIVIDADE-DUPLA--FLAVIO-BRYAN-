import os
os.system("cls")

numeros = []
quantidade_numerica = 10

for i in range(quantidade_numerica):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    positivos = [num for num in numeros if num > 0]
print("\nVetor com apenas os positivos:", positivos)
print(f"Quantidade de elementos copiados: {len(positivos)}")