import os
os.system("cls")

numeros = []
quantidade_numerica = 10
for i in range(quantidade_numerica):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
print("\nVetor original:", numeros)

transformados = [num * 2 if num % 2 == 0 else num * 3 for num in numeros]
print("Vetor transformado:", transformados)