import os
os.system

print("Feito por: Bryan")
print("R.A.: 026.082365")

vetor_temperaturas = []
import os
os.system("cls")

for i in range(1, 8):
    temperatura = float(input(f"\nDigite a temperatura do {i}º dia da semana (°C): "))
    vetor_temperaturas.append(temperatura)

os.system('cls')
print("\n--- TEMPERATURAS REGISTRADAS ---")

posicao = 1
for temp in vetor_temperaturas:
    print(f"\n{posicao}º dia: {temperatura:.1f}°C")
    posicao += 1

media = sum(vetor_temperaturas) / 7
maior_temp = max(vetor_temperaturas)
menor_temp = min(vetor_temperaturas)

print("-" * 32)
print(f"\nMédia da semana: {media:.1f}°C")
print(f"Maior temperatura: {maior_temp:.1f}°C")
print(f"Menor temperatura: {menor_temp:.1f}°C")
