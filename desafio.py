
lista = """ 

[0] depositar
[1] sacar 
[2] extrato
[3] sair

=>"""
saldo = 1500.0
limite = 500
extrato = ""
numeros_saques = 0 + 1 
LIMITE_SAQUESss = 3

while True: 

    opcao = input(lista)

    if opcao == "0":
        valor = float(input("informe o deposito: "))

        if valor > 0: 
            saldo += valor 
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
           print("operaçao falhou, o valor dado foi invalido")
    elif opcao == "1":

        valor = float(input("informe o saque: "))

        excedeu_saldo = valor >= saldo
        
        excedeu_limite = valor >= limite 

        excedeu_saque = numeros_saques >= LIMITE_SAQUESss

        if excedeu_saldo:
            print("Operação falhou, voçê não tem saldo suficiente")
        
        if excedeu_limite:
            print("Operação falhou, o valor de saque excede o limite")
        
        if excedeu_saque:
            print("Operação falhou, voçê excedeu o limites de saques diarios")

        elif valor > 0:
            saldo -= valor
            extrato += (f"saque: R${valor:.2F}\n")
            numeros_saques += 1

        else:
            print("Operação falhou, o valor informado é invalido! ")

    elif opcao == "2":
        print ("\n===========EXTRATO===========")
        print("Não foram realizadas movimentações. ") if not extrato else extrato
        print(f'\nSaldo: R$ {saldo:.2f}') 
        print("================================")
    elif opcao == "3":
        break

    else:
        print("Operação invalida, por favor selecione operação desejada")























