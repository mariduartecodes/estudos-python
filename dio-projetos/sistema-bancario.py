# Menu e variaveis

menu = """Menu de opções:

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

Digite a opção -> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

# Depósito 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito: R$ {valor:.2f}\nSaldo atual: R$ {saldo:.2f}")

        else:
            print("Valor inválido. O depósito deve ser um valor positivo.")

# Saque

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. Tente novamente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. Tente novamente.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. Tente novamente.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque: R$ {valor:.2f} | Saques restantes: {LIMITE_SAQUES - numero_saques}\nSaldo atual: R$ {saldo:.2f}")


# Extrato

    elif opcao == "e":
        print("============== EXTRATO ==============\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"SALDO TOTAL: R$ {saldo:.2f}\n")
        print("=====================================")

    elif opcao == "q":
        print("Obrigada por usar nosso sistema!\n""" )
        break

# Error

    else:
        print("Opção inválida, digite uma opção válida:")
