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
            print("Valor Depositado com Sucesso.")
        
        else:
            print("O Valor Informado é Inválido.")

    elif opcao == "s":
        
        valor = float(input("Informe o Valor do Saque: \n"))
        
        if numero_de_saques == limite_de_saques:
        
            print("O Número Máximo de Saques foi alcançado. \n")
        
        else:
            
            if saldo < valor:
                print("Valor Insuficiente na conta. \n") 
            
            else: 
                
                if valor > 0 and valor < 501:
                    numero_de_saques += 1
                    extrato += f"Saque: R$ {valor:.2f} \n"
                    saldo -= valor
                    print("Valor Sacado com Sucesso.")
                
                else: 
                    print("O Valor Informado é Inválido. \n")

    elif opcao == "e":
        print("\n--------Extrato--------")
        print("Não Foram Realizadas Movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------")

    elif opcao == "q":
        print("O Programa Foi Encerrado. \n")
        break
    
    else:
        print("Selecione Novamente a Operação Desejada.")
