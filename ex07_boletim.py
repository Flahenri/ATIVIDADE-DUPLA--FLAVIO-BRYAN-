import os
os.system("cls")

soma_notas = 0

for i in range(3):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota (0 a 10): "))
        if 0 <= nota <= 10:
            break
        print("Nota inválida! Digite um valor entre 0 e 10.")
    soma_notas += nota

media = soma_notas / 3

print(f"\nMédia final: {media:.1f}")

if media >= 7:
    print("Situação: aprovado")
elif 5 <= media < 7:
    print("Situação: recuperação")
else:
    print("Situação: reprovado")