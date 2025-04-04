#projeto para excutar operações bancárias.
#Regras: executar operações: 
#depositar - regra: apenas valores positivos
#sacar - regra: até 3 saques sendo cada saque limitados a R$ 500,00 no total (barrar saque único acima de R$500)
        #regra 2: se não tiver saldo, exibir msg informando que não será possível sacar por falta de saldo
#extrato: regra: conter todas as operações de depósito e saque no formato: R$ x.xxx,xx
#Sair


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:  #verifica se o valor do deposito é positivo
            saldo += valor   #adiciona o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"   #concatena para adicionar ao extrato

        else:
            print("Operação falhou! O valor informado é inválido.")  #exibir para valor negativo

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo  #verifica saldo

        excedeu_limite = valor > limite   #verifica limite de 500,00

        excedeu_saques = numero_saques >= LIMITE_SAQUES #verifica lime de saques (3 saques)

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:   #se estiver tudo ok quanto a limite (saque e valor), verifica valor se é positivo
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"  #registra no extrato
            numero_saques += 1    #contador pra saque

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)   #verifica se extato está vazio
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":  #operação de saída
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  #selação não reconhecida