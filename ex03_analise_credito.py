import os
os.system("cls")

print("=" * 45)
print(" PRÉ-ANÁLISE DE CRÉDITO - FINANCEIRA CONFIA   ")
print("=" * 45)

renda_mensal = float(input("Renda mensal do cliente (R$): "))
valor_emprestimo = float(input("Valor do empréstimo solicitado (R$): "))
num_prestacoes = int(input("Número de prestações desejadas: "))
valor_prestacao = valor_emprestimo / num_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

print("\n" + "-" * 40)
print(f"Valor da Prestação: R$ {valor_prestacao:.2f}")
print("-" * 40)
if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("SITUAÇÃO: CRÉDITO APROVADO! 🎉")
    print("O cliente atende a todos os requisitos de segurança.")
else:
    print("SITUAÇÃO: CRÉDITO NEGADO! ❌")
    print("Motivo(s) da reprovação:")
    if valor_emprestimo > limite_emprestimo:
        print(f" - O empréstimo excede o limite máximo de 10x a renda (Máx: R$ {limite_emprestimo:.2f})")
    if valor_prestacao > limite_prestacao:
        print(f" - A prestação excede 30% da renda mensal (Máx: R$ {limite_prestacao:.2f})")
print("-" * 40)
