import os
os.system("cls")

vetor_A = []
vetor_B = []
vetor_C = []

for i in range(5):
    vetor_A.append(int(input(f"Digite o {i+1}º número do vetor A: ")))
    vetor_B.append(int(input(f"Digite o {i+1}º número do vetor B: ")))
    vetor_C.append(vetor_A[i] + vetor_B[i])

print(f"\nVetor A: {vetor_A}")
print(f"Vetor B: {vetor_B}")
print(f"Vetor C (Soma): {vetor_C}")