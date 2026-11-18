import os
os.system("cls")

idades = []
maiores_de_idade = 0

for i in range(5):
    while True:
        idade = int(input(f"Digite a idade da {i+1}ª pessoa (0 a 120): "))
        if 0 <= idade <= 120:
            idades.append(idade)
            if idade >= 18:
                maiores_de_idade += 1
            break
        print("Idade inválida! Tente novamente.")

maior = max(idades)
menor = min(idades)

print(f"\nMaior idade: {maior} anos")
print(f"Menor idade: {menor} anos")
print(f"Quantidade de maiores de idade: {maiores_de_idade}")