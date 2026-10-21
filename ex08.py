import os
os.system("cls")

nomes = []
salarios = []
bonus = 0

for i in range(5):
    nomes.append(input(f"Nome do {i+1}º funcionário: "))
    salario = float(input(f"Salário do {i+1}º funcionário: "))
    salarios.append(salario)
    if salario > 2000:
        bonus += 1

maior_salario = max(salarios)
ganhadores_maior = [nomes[i] for i, sal in enumerate(salarios) if salario == maior_salario]

print(f"\nMaior salário: R$ {maior_salario:.2f}")
print(f"Quem recebe o maior salário: {', '.join(ganhadores_maior)}")
print(f"Ganham acima de R$ 2.000,00: {bonus} funcionário(s)")
