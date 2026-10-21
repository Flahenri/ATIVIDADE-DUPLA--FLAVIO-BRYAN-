import os
os.system("cls")
from colorama import Back, Fore, init, Style

clientes = [" Ana Souza", "Carlos Silva", "Marcos Oliveira", "Thiago André", "Paulo Henrique", "Juliana Silva ", ]

print("=" *67 )
print(Fore.GREEN + Style.BRIGHT + "    REVOLUCIONE A CAPTAÇÃO DO SEU CONSÓRCIO COM AUTOFLOW! 🎯🚀" + Style.RESET_ALL)
print("=" *67 )
print(Fore.CYAN + Style.BRIGHT + "Encontrar o perfil ideal não precisa ser um jogo de adivinhação.")
print("Conecte sua oferta diretamente a quem já está pronto para comprar")
print("O AutoFlow qualifica leads, organiza a jornada de vendas e garante")
print("que sua equipe foque no que importa: converter e fechar contratos." + Style.RESET_ALL)
print("=" *67)
print()
print(Fore.GREEN + Style.BRIGHT + "• Clientes Certo na hora certa ✨.") 
print("• Clientes Aguardando Notificação ✅." + Style.RESET_ALL)
print()
opcao = input(">>> Deseja enviar notificação via WhatsApp para o primeiro cliente? (S/N): ").strip().upper()

match opcao:
    case "S":
        cliente_avisado = clientes.pop(0)
        print(Fore.BLUE + f"\n[+] Enviando WhatsApp para {cliente_avisado}..." + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + "SUCESSO! Notificação enviada e registrada no histórico ✅!" + Style.RESET_ALL)
        print(Fore.BLUE + f"Fila atualizada de clientes aguardando: {clientes}" + Style.RESET_ALL)
    case "N":
        print(Fore.YELLOW + "\nAtendimento suspenso. O cliente permanece na fila de espera." + Style.RESET_ALL)
    case _:
        print(Fore.RED + Style.BRIGHT + "\nOpção inválida. Operação cancelada." + Style.RESET_ALL)