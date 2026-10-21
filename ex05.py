import os
os.system("cls")

notas = []
quantidade_numerica = 5

for i in range(quantidade_numerica):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acima_da_media = sum(1 for nota in notas if nota > media)
print("\nNotas digitadas:", notas)
print(f"Média da turma: {media:.2f}")
print(f"Quantidade de notas acima da média: {acima_da_media}")