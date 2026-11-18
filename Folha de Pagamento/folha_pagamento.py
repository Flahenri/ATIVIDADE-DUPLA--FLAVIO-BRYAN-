import os
os.system("cls")

largura = 67
matricula_cadastrada = ""
senha_cadastrada = ""

def menu_cadastro():
    print("=" * largura)
    print("Sistema de Recursos Humanos - Primeiro Acesso")
    print("Crie seu número de matrícula e sua senha")
    print("=" * largura)

def menu_login():
    os.system("cls")
    print("=" * largura)
    print("Sistema de Recursos Humanos - Folha de Pagamento")
    print("Insira seu número de matrícula e sua senha salva")
    print("=" * largura)

def menu_dados():
    os.system("cls")
    print("=" * largura)
    print("Sistema de Recursos Humanos - Dados do Funcionário")
    print("Preencha as informações solicitadas abaixo")
    print("=" * largura)

def cadastrar_acesso():
    menu_cadastro()
    
    mat = input("Crie sua matrícula: ").strip()
    while mat == "":
        print("Erro: a matrícula não pode ficar em branco.")
        mat = input("Crie sua matrícula: ").strip()
    
    sen = input("Crie sua senha: ").strip()
    while sen == "":
        print("Erro: a senha não pode ficar em branco.")
        sen = input("Crie sua senha: ").strip()
    
    return mat, sen

def autenticar(mat_digitada, sen_digitada):
    if mat_digitada == matricula_cadastrada and sen_digitada == senha_cadastrada:
        return "sim"
    return "nao"

def realizar_login():
    tentativas = 0
    max_tentativas = 3
    
    menu_login()
    
    while tentativas < max_tentativas:
        mat_digitada = input("Digite sua matrícula: ").strip()
        sen_digitada = input("Digite sua senha: ").strip()
    
        if autenticar(mat_digitada, sen_digitada) == "sim":
            print("\nAcesso liberado!\n")
            return "sim"
        else:
            tentativas += 1
            restantes = max_tentativas - tentativas
            if restantes > 0:
                print(f"\nMatrícula ou senha incorretas! Você ainda tem {restantes} tentativa(s).\n")
            else:
                print("\nNúmero máximo de tentativas atingido. Programa encerrado!")
                return "nao"

def coletar_dados():
    menu_dados()
    
    salario_valido = "nao"
    while salario_valido == "nao":
        try:
            salario_base = float(input("Digite o salário base (R$): ").replace(",", "."))
            if salario_base <= 0:
                print("Valor inválido! O salário deve ser maior que zero.")
            else:
                salario_valido = "sim"
        except ValueError:
            print("Erro! Digite apenas números para o salário (ex: 1621 ou 1621.00).")
        
    quer_vt = input("Deseja vale-transporte? (s/n): ").strip().lower()
    while quer_vt != "s" and quer_vt != "n":
        print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")
        quer_vt = input("Deseja vale-transporte? (s/n): ").strip().lower()
    
    vr_valido = "nao"
    while vr_valido == "nao":
        try:
            valor_vr = float(input("Digite o valor do vale-refeição pago pela empresa (R$): ").replace(",", "."))
            if valor_vr < 0:
                print("Valor inválido! O vale-refeição não pode ser negativo.")
            else:
                vr_valido = "sim"
        except ValueError:
            print("Erro! Digite apenas números para o vale-refeição.")
        
    dep_valido = "nao"
    while dep_valido == "nao":
        try:
            dependentes = int(input("Digite a quantidade de dependentes: "))
            if dependentes < 0:
                print("Quantidade inválida! Digite zero ou um número positivo.")
            else:
                dep_valido = "sim"
        except ValueError:
            print("Erro! Digite apenas um número inteiro para dependentes (ex: 0, 1, 2).")
        
    return salario_base, quer_vt, valor_vr, dependentes

def calcular_inss(salario_base):
    if salario_base >= 8475.55:
        return 988.10
    
    desconto = 0.0
    
    if salario_base > 1621.00:
        desconto += 1621.00 * 0.075
    else:
        desconto += salario_base * 0.075
        return desconto
    
    if salario_base > 2902.84:
        desconto += (2902.84 - 1621.00) * 0.09
    else:
        desconto += (salario_base - 1621.00) * 0.09
        return desconto
    
    if salario_base > 4354.27:
        desconto += (4354.27 - 2902.84) * 0.12
    else:
        desconto += (salario_base - 2902.84) * 0.12
        return desconto
    
    desconto += (salario_base - 4354.27) * 0.14
    return desconto

def calcular_irrf(salario_base, inss, dependentes):
    base = salario_base - inss - (dependentes * 189.59)

    if base <= 2428.80:
        imposto = 0.0
    elif base <= 2826.65:
        imposto = (base * 0.075) - 182.16
    elif base <= 3751.05:
        imposto = (base * 0.15) - 394.16
    elif base <= 4664.68:
        imposto = (base * 0.225) - 675.49
    else:
        imposto = (base * 0.275) - 908.73
    
    if salario_base <= 5000.00:
        imposto = 0.0
    elif salario_base <= 7350.00:
        reducao = 978.62 - (0.133145 * salario_base)
        imposto = imposto - reducao
    
    if imposto < 0:
        imposto = 0.0
    
    return imposto

def calcular_vt(salario_base, quer_vt):
    if quer_vt == "s":
        return salario_base * 0.06
    return 0.0

def calcular_vr(valor_vr):
    return valor_vr * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def mostrar_contracheque(matricula, salario_base, quer_vt, valor_vr, dependentes, inss, irrf, vt, vr, saude):
    os.system("cls")
    
    total_descontos = inss + irrf + vt + vr + saude
    salario_liquido = salario_base - total_descontos
    
    if quer_vt == "s":
        texto_vt = "Sim"
    else:
        texto_vt = "Não"
    
    print("=" * largura)
    print(f"CONTRACHEQUE • MATRÍCULA {matricula}")
    print("=" * largura)
    print(f"Salário base:          R$ {salario_base:.2f}")
    print("-" * largura)
    print(f"(-) INSS:              R$ {inss:.2f}")
    print(f"(-) IRRF:              R$ {irrf:.2f}")
    print(f"(-) Vale-transporte:   R$ {vt:.2f}")
    print(f"(-) Vale-refeição:     R$ {vr:.2f}")
    print(f"(-) Plano de saúde:    R$ {saude:.2f}")
    print("-" * largura)
    print(f"Total de descontos:    R$ {total_descontos:.2f}")
    print("=" * largura)
    print(f"SALÁRIO LÍQUIDO:       R$ {salario_liquido:.2f}")
    print("=" * largura)
    print("BENEFÍCIOS ESCOLHIDOS:")
    print(f"Vale-transporte: {texto_vt} | Valor VR empresa: R$ {valor_vr:.2f} | Dependentes: {dependentes}")
    print("=" * largura)

matricula_cadastrada, senha_cadastrada = cadastrar_acesso()

acesso_liberado = realizar_login()

if acesso_liberado == "sim":
    salario_base, quer_vt, valor_vr, dependentes = coletar_dados()
    
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, inss, dependentes)
    vt = calcular_vt(salario_base, quer_vt)
    vr = calcular_vr(valor_vr)
    saude = calcular_plano_saude(dependentes)
    
    mostrar_contracheque(matricula_cadastrada, salario_base, quer_vt, valor_vr, dependentes, inss, irrf, vt, vr, saude)