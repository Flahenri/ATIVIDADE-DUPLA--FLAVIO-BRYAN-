import os
os.system("cls")

print("=" * 40)
print("   MUNDO ELETRO - MÓDULO DE CHECKOUT     ")
print("=" * 40)

valor_produto = float(input("Valor do produto (R$): "))
print("\n[1] À Vista")
print("[2] A Prazo")
forma_pagamento = input("Escolha a forma de pagamento: ")

desconto = 0.0
total_a_pagar = valor_produto
quantidade_parcelas = 1
valor_parcela = valor_produto
opcao_valida = True
if forma_pagamento == "1":
    desconto = valor_produto * 0.10
    total_a_pagar = valor_produto - desconto
    valor_parcela = total_a_pagar
    txt_forma = "À Vista (com 10% de desconto)"
elif forma_pagamento == "2":
    quantidade_parcelas = int(input("Digite a quantidade de parcelas (Máximo 6): "))
    
    if quantidade_parcelas > 6 or quantidade_parcelas < 1:
        print("\n❌ Erro: Quantidade de parcelas inválida! Permitido de 1 a 6 vezes.")
        opcao_valida = False
    else:
        valor_parcela = valor_produto / quantidade_parcelas
        txt_forma = f"A Prazo ({quantidade_parcelas}x)"
else:
    print("\n❌ Erro: Opção de pagamento inválida!")
    opcao_valida = False
if opcao_valida:
    print("\n" + "-" * 40)
    print("           CUPOM FISCAL DE VENDA           ")
    print("-" * 40)
    print(f"Valor Original:    R$ {valor_produto:.2f}")
    print(f"Forma Pagamento:   {txt_forma}")
    
    if forma_pagamento == "1":
        print(f"Desconto Aplicado: R$ {desconto:.2f}")
    else:
        print(f"Valor da Parcela:  R$ {valor_parcela:.2f}")
        
    print(f"TOTAL A PAGAR:     R$ {total_a_pagar:.2f}")
    print("-" * 40)
