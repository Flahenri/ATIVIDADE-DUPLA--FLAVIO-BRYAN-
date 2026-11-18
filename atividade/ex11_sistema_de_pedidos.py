import os
os.system("cls")


total_pagar = 0.0
quantidade_pratos = 0


print( "=" *40)
print("      Restaurante Sabor de Casa ☀️")
print("=" *40)

while True:
    print('''
|=============================================|
|     📝 Cardápio Resturante Sabor de Casa.   |
| Código    |     Pratos     |     Valor (R$) |
|---------------------------------------------|
|1          |     Picanha    |      25,00     |
|2          |     Lasanha    |      20,00     |
|3          | Bife Acebolado |      15,00     |
|4          |   Pão com Ovo  |       5,00     |
|=============================================|''')
    opcao = int(input("Insira uma das opções: "))
    
    match opcao:
        case 1:
            total_pagar = 25.00
            quantidade_pratos = 1
            print("Picanha adicionado!")
        case 2:
            total_pagar = 20.00
            quantidade_pratos = 1
            print("Lasanha adicionado!")
        case 3:
            total_pagar = 15.00
            quantidade_pratos = 0
            print("Bife Acebolado Adicionado!")
        case 4:
            total_pagar = 5.00
            quantidade_pratos = 1
            print("Pão com ovo Adicionado!")
        case _:
            print("Código inválido! Nenhum prato foi adicionado.")
            continue
    resposta = input("Deseja outro prato? (S/N): ").upper()
    if resposta == "N":
        break

print(f"\nQuantidade total de pratos: {quantidade_pratos}")
print(f"Total a pagar: R$ {total_pagar:.2f}")