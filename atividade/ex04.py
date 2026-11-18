import os
os.system("cls")

vetor = []

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

pesquisa = int(input("\nDigite um número para pesquisar: "))

if pesquisa in vetor:
    posicao = vetor.index(pesquisa)
    print(f"O número existe e está na posição {posicao}.")
else:
    print("Número não encontrado.")