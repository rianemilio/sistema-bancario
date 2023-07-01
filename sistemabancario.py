menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o Valor do Depósito: \n"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
            print("Valor Depositado com Sucesso")
        else:
            print("O Valor Informado é Inválido")

    elif opcao == "s":
        valor = float(input("Informe o Valor do Saque: \n"))
        if saldo >= valor:
            if valor > 0 and valor < 501 and numero_de_saques != limite_de_saques:
                numero_de_saques += 1
                extrato += f"Saque: R$ {valor:.2f} \n"
                saldo -= valor
                print("Valor Sacado com Sucesso")
            else: 
                print("O Valor Informado é Inválido \n")
        else:
            print("Valor Insuficiente na conta \n")
    
    elif opcao == "e":
        print(extrato) 

    elif opcao == "q":
        print("O Programa Foi Encerrado \n")
        break
