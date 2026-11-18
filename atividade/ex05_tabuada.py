import os
import time

os.system("cls")

print("=" * 40)
print("     APP REFORÇO ESCOLAR - APRENDER+     ")
print("=" * 40)

numero = int(input("Digite o número para ver a tabuada: "))

print("\n" + "-" * 40)
print(f"       TABUADA DE MULTIPLICAÇÃO DO {numero}       ")
print("-" * 40)
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    time.sleep(1)

print("-" * 40)
print("Tabuada gerada com sucesso! Estude bastante! 📚")
