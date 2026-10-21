import os
os.system("cls")

temperaturas = []

for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)

print("\nTemperaturas registradas:")

for i in range(7):
    print(f"Dia {i+1}: {temperaturas[i]}°C")

print(f"\nMédia semanal: {media:.2f}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")