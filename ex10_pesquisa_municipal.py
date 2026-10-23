import os
os.system("cls")

total_familias = 0
soma_salarios = 0.0
soma_filhos = 0

maior_salario = None
menor_salario = None

while True:
    print("\n--- Sistema da Pesquisa Municipal ---")
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        salario = float(input("Digite o salário da família (R$): "))
        num_filhos = int(input("Digite o número de filhos: "))
        
        total_familias += 1
        soma_salarios += salario
        soma_filhos += num_filhos
        
        if maior_salario is None or salario > maior_salario:
            maior_salario = salario
            
        if menor_salario is None or salario < menor_salario:
            menor_salario = salario
            
        print("Família adicionada com sucesso!")
        
    elif opcao == "2":
        break
    else:
        print("Opção inválida! Por favor, escolha 1 ou 2.")

os.system("cls")
print("="*30)
print("       RESULTADOS DA PESQUISA     ")
print("="*30)
print(f"Total de famílias pesquisadas: {total_familias}")

if total_familias > 0:
    media_salario = soma_salarios / total_familias
    media_filhos = soma_filhos / total_familias
    
    print(f"Média de salário das famílias: R$ {media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.1f}")
    print(f"Maior salário informado: R$ {maior_salario:.2f}")
    print(f"Menor salário informado: R$ {menor_salario:.2f}")
else:
    print("Nenhuma família foi registrada na pesquisa.")
print("="*30)