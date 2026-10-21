import os
os.system("cls")

vetor_numeros = []
quantidade_numerica = 4

for i in range (quantidade_numerica):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor_numeros.append(num)
print()
print("Ordem Digitadas: ")
for num in vetor_numeros:
    print(num, end= " ")
print()
print("Ordem Inversa: ")
for num in reversed(vetor_numeros):
    print(num, end=" ")
print()

