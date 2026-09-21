# Função para depositar
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


# Função para sacar
def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")

    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        print("Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


# Função para exibir extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")

    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)

    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================\n")


# Função para criar usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")

    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Operação falhou! Já existe um usuário com esse CPF.")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }

    usuarios.append(usuario)

    print("Usuário criado com sucesso!")


# Função para criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    usuario = None

    for usuario_cadastrado in usuarios:
        if usuario_cadastrado["cpf"] == cpf:
            usuario = usuario_cadastrado
            break

    if usuario is None:
        print("Operação falhou! Usuário não encontrado.")
        return None

    conta = {
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario,
    }

    print("Conta criada com sucesso!")
    print(f"Agência: {agencia}")
    print(f"Número da conta: {numero_conta}")
    print(f"Titular: {usuario['nome']}")

    return conta


# Função para listar contas
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n================ CONTAS ================")

    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print("----------------------------------------")

    print("========================================")


# Menu
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar usuário
[a] Criar conta
[l] Listar contas
[q] Sair

=> """


# Variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

AGENCIA = "0001"
numero_conta = 1


# Programa principal
while True:

    opcao = input(menu)

    # Depositar
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(
            saldo,
            valor,
            extrato
        )

    # Sacar
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = sacar(
            saldo,
            valor,
            extrato,
            limite,
            numero_saques,
            LIMITE_SAQUES
        )

    # Extrato
    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    # Criar usuário
    elif opcao == "c":
        criar_usuario(usuarios)

    # Criar conta
    elif opcao == "a":
        conta = criar_conta(
            AGENCIA,
            numero_conta,
            usuarios
        )

        if conta:
            contas.append(conta)
            numero_conta += 1

    # Listar contas
    elif opcao == "l":
        listar_contas(contas)

    # Sair
    elif opcao == "q":
        print("Obrigada por usar nosso sistema!")
        break

    # Opção inválida
    else:
        print("Operação inválida. Por favor, selecione novamente.")