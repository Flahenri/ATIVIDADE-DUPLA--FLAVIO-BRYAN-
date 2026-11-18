import os
os.system("cls")

login_salvo = input("Cadastre seu login: ")
senha_salva = input("Cadastre sua senha: ")

os.system("cls")

tentativas = 0

while tentativas < 3:
    login_tentativa = input("Digite seu login para entrar: ")
    senha_tentativa = input("Digite sua senha para entrar: ")
    
    if login_tentativa == login_salvo and senha_tentativa == senha_salva:
        print("Bem-vindo ao sistema da Clínica VidaPlena!")
        break
    else:
        tentativas += 1
        print(f"Login ou senha incorretos! Essa foi a sua tentativa número: {tentativas}")

if tentativas == 3:
    print("Acesso bloqueado por excesso de tentativas!")