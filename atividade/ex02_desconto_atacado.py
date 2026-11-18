import os
os.system("cls")

print("=" * 40)
print(" SISTEMA DE CAIXA - ATACAREJO BOM PREÇO  ")
print("=" * 40)

produto = input("Nome do produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unitario = float(input("Preço unitário (R$): "))

total_bruto = quantidade * preco_unitario

if quantidade <= 5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05

valor_desconto = total_bruto * percentual_desconto
total_a_pagar = total_bruto - valor_desconto

print("\n" + "-" * 40)
print(f"Produto: {produto}")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto ({percentual_desconto * 100:.0f}%): R$ {valor_desconto:.2f}")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
print("-" * 40)
