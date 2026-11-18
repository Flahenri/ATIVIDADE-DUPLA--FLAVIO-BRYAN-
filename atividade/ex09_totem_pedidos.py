import os
os.system("cls")

total_pagar = 0.0
quantidade_pratos = 0

while True:
    print("\n--- CARDÁPIO RESTAURANTE RESTAURANTE DO SEU ZÉ ---")
    print("1 - Sushi - R$ 25.00")
    print("2 - espaguette - R$ 22.00")
    print("3 - Feijoada - R$ 30.00")
    print("4 - Salada - R$ 18.00")
    print("5 - Lasanha - R$ 24.00")
    
    opcao = input("\nDigite o código do prato desejado: ")
    
    match opcao:
        case "1":
            total_pagar += 22.00
            quantidade_pratos += 1
            print("Sushi adicionado!")
        case "2":
            total_pagar += 25.00
            quantidade_pratos += 1
            print("Espaguette adicionada!")
        case "3":
            total_pagar += 30.00
            quantidade_pratos += 1
            print("Feijoada adicionada!")
        case "4":
            total_pagar += 18.00
            quantidade_pratos += 1
            print("Salada adicionada!")
        case "5":
            total_pagar += 24.00
            quantidade_pratos += 1
            print("Lasanha adicionada!")
        case _:
            print("Código inválido! Nenhum prato foi adicionado.")
            continue

    resposta = input("Deseja outro prato? (S/N): ").upper()
    if resposta == "N":
        break

print(f"\nQuantidade total de pratos: {quantidade_pratos}")
print(f"Total a pagar: R$ {total_pagar:.2f}")