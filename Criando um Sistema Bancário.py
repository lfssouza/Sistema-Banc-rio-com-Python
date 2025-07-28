menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 501
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        try:
            valor_deposito = float(input("Valor a ser depositado: "))

        except ValueError:
            print("Valor inválido")
            continue

        concluir = input(f"Deseja depositar o valor: R${valor_deposito:.2f}? (S/N) \n").strip().upper()
        
        if concluir == "S":
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(f"Valor de {valor_deposito:.2f}, foi depósitado com sucesso!")
            else:
                print("Operação falhou")
        else:
            print("Deposito cancelado")
    
    elif opcao == "2" :
        if numero_saques < LIMITE_SAQUES:
            if saldo <= 0:
                print("Saldo insuficiente")
                continue

            try:
                valor_saque = float(input("Valor que deseja sacar: "))
            except ValueError:
                print("Informação inválida")
                continue
            
            prosseguir = input(f"Deseja sacar o valor: R${valor_saque:.2f}? (S/N) \n").strip().upper()

            if prosseguir == "S":
                if valor_saque <= saldo:
                    if valor_saque < limite:
                        saldo -= valor_saque
                        extrato += f"Saque: R${valor_saque:.2f}\n"
                        numero_saques += 1
                        print(f"Valor de R$ {valor_saque:.2f}, foi sacado com sucesso!")

                    else:
                        print("Valor acima do limite de R$500")
                else:
                    print("Valor acima do seu saldo")

            else:
                print("Saque cancelado")
            
        else:
            print("Limite de saques diários atingidos!")
    
    elif opcao == "3" :
        if not extrato:
            print("Não foram realizadas movimentações.")
        
        else:
            print(f"Seu extrato é:\n\n{extrato}")

            print(f"O saldo atual da conta: R$ {saldo:.2f}")
    elif opcao == "0" :
        break

    else:
        print("Operação inválida, por favor selecionar uma opção existente")
