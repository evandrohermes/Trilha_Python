menu = """
Bem vindo, Escolha a opção desejada:

[1] Saldo
[2] Extrato
[3] Depósito
[4] Saque
[0] Sair

=> """

saldo_conta = 0
valor_limite_saque = 500
extrato_conta = ""
numero_saques_diarios = 0
LIMITE_SAQUES_DIARIOS = 3

while True:

    operacao = input(menu)

    if operacao == "1":
        print("\n----- SALDO DA CONTA -----")
        print(f"\nSaldo atual: R$ {saldo_conta:2.2f}")
        print("----------------------------")

    elif operacao == "2":
        print("\n---- EXTRATO BANCARIO ----")
        print("Não existem movimentações para serem exibidas." if not extrato_conta else extrato_conta)
        print(f"\nSaldo atual: R$ {saldo_conta:2.2f}")
        print("----------------------------")
    
    elif operacao == "3":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo_conta += valor
            extrato_conta += f"Crédito: R$ {valor:2.2f}\n"

        else:
            print("Não foi possível realizar a operação! O valor informado é inválido.")

    elif operacao == "4":
        valor = float(input("Informe o valor que deseja sacar: "))
        
        erro_saque_saldo = valor > saldo_conta

        erro_saque_valor = valor > valor_limite_saque

        erro_saque_limite = numero_saques_diarios >= LIMITE_SAQUES_DIARIOS
        
        if erro_saque_saldo:
            print("Não foi possível realizar a retirada! Saldo suficiente.")

        elif erro_saque_valor:
            print("Não foi possível realizar a retirada! Valor do saque maior que o permitido.")

        elif erro_saque_limite:
            print("Não foi possível realizar a retirada! Você já atingiu o número máximo de saques diários.")

        elif valor > 0:
            saldo_conta -= valor
            extrato_conta += f"Débito:  R$ {valor:2.2f}\n"
            numero_saques_diarios += 1

        else:
            print("Operação não realizada! Valor informado inválido.")

    elif operacao == "0":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")
