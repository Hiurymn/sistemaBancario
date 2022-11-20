#Sitema Bancario
from time import sleep
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3
saque = 0
while True:

    opçao = input(menu)

    if opçao == 'd':
        print('Deposito')

        deposito_diario = float(input('Qual o valor do deposito? '))

        if (deposito_diario > 0):
            saldo += deposito_diario
            sleep(2)
            print(f'DEPOSITO DE R${deposito_diario} REALIZADO COM SUCESSO!')
        else:
            print('Valor do Deposito Inválido')

    elif opçao == 's':
        print('Saque')
        if numero_saque == LIMITE_SAQUES:
            sleep(1)
            print('Limite diario de Saque Atigindo')
        else:
            if saldo == 0:
                print('Saldo Insuficiente')
            else:
                saque_dia = float(input('Valor do Saque: '))
                if saldo > 0 and saque_dia <= 500:
                    saldo -= saque_dia
                    sleep(2)
                    print(f'SAQUE DE R${saque_dia} SOLICITADO COM SUCESSO! AGUARDE A CONTAGEM DAS NOTAS..')
                    numero_saque += 1
                    saque += 1

                else:
                    print(f'Saldo Insuficiente, ou limite diario de R${limite} atigido')
    elif opçao == 'e':

        print('\n************************ ESTRATO ************************')
        sleep(2)
        print(f'Saldo: R${saldo}')
        if saque == 0:

            print(f'Saque: {saque_dia}')
        else:
            print(f'{saque} saques, Ultimo saque de R${saque_dia}')
        print('*********************************************************')
    elif opçao == 'q':
        break
    else:
        print('Operação Invalida, Por favor selecione novamente a operação desejada')

