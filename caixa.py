
deposito = 0
saldo = 0
saque = 0

extrato = ''

VALOR_SAQUE_MAX = 500
LIMITE_SAQUE_DIARIO = 3



while True:

    menu = int(input(
    """
    =====================================
                opcoes
    *************************************
        [1] - Deposito
        [2] - extrato
        [3] - saque
        [4] - sair

    =====================================
    -> 
    """
    ))

    if menu == 1:
        deposito = float(input('Deposito:  '))
        if deposito <= 0:
            print('Valor digitado incorreto. Tente depositar novamente...')
        else:
            saldo += deposito
            extrato += f'Valor depositado {deposito} \n'
            print(f'Seu saldo atual e de R$ {saldo:.2f}')
    elif menu == 2:
        print(f'Saldo atual e de R$ {extrato:.2f}')
    elif menu == 3:
        if LIMITE_SAQUE_DIARIO == 0:
            print('Voce escedeu o limite de saques diario... Tente novamente amanha...')
        else:
            saque = float(input('Digite o valor de saque:  '))
            if (saque <= 0) or (saque > saldo) or (saque > VALOR_SAQUE_MAX):
                print('Nao sera possivel sacar o dinheiro por falta de saldo!!!')
            else:
                print(f'Seu saldo atual e de R$ {saldo:.2f} - {saque:.2f} = {saldo-saque:.2f}')
                saldo -= saque
                print(f'Seu saque foi de {saque:.2f}')
                LIMITE_SAQUE_DIARIO -=1
                extrato += f'Valor sacado R$ {saque} \n'2
    elif menu == 4:
        break
