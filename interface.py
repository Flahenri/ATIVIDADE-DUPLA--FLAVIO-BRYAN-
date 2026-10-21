import os
os.system("cls")
from colorama import Back, Fore, init, Style

clientes = ["Ana Souza", "Carlos Silva", "Marcos Oliveira"]

print("=" *58 )
print("REVOLUCIONE A CAPTAÇÃO DO SEU CONSÓRCIO COM AUTOFLOW! 🎯🚀")
print("=" *58 )
print()
print("Encontrar o perfil ideal não precisa ser um jogo de adivinhação.")
print("Conecte sua oferta diretamente a quem já está pronto para comprar")
print("O AutoFlow qualifica leads, organiza a jornada de vendas e garante")
print("que sua equipe foque no que importa: converter e fechar contratos.")
print()
print("=" *67)
print()
print("Clientes Certo na hora certa ✨.")
print("Clientes Aguardando Notificação ✅.")
print()

opcao = input("Deseja enviar aviso para o primeiro cliente (S/N): ").upper()

match opcao:
    case "S":
        cliente_avisado = clientes[0]
        print(f"Enviando Whatsapp para {cliente_avisado}...")
        print("SUCESSO! Notificação enviada e salva no histórico!")
    case "N":
        print("Atendimento cancelado. O cliente continua na lista de espera.")
    case _:
        print("Opção inválida. Tente Novamente.")