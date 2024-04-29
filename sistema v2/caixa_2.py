
def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Passou aqui === {saldo} e \n{extrato}')
        return saldo, extrato

    else:
        print("Operação falhou! O valor informado é inválido.")

def saque(*, valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES):            
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return saldo, extrato, numero_saques

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")


def func_extrato(saldo, /, *, extrato):    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# Funcoes relacionadas ao usuario

def criar_usuario(*cadastros):
    cpf = input('CPF: ')
    
    
    if cpf in cadastros:
        print('CPF ja esta cadastrado...')
        print('Cadastre outro CPF...')
    else:
        nome = input('Nome: ')
        data_nascimento = input('Data de nascimento: ')
        logradouro = input('Logradouro: ')
        numero_casa = input('Numero da Casa: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado Sigla (ex: SP): ')
        endereco = f'{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}'
        return dict(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    
def criar_conta_corrente(numero_conta_anterior):
    cliente = input('Cpf: ')
    numero_da_conta = numero_conta_anterior +1
    numero_agencia = '0001'
    return dict( numero_agencia=numero_agencia, numero_da_conta=numero_da_conta, cliente=cliente)

def listar_contas():
    pass


# -------------------------- DADOS DO BANCO E VARIAVEIS
if __name__ == "__main__":

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = 50
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    numero_de_contas = 0 # numero das contas do banco

    clientes = []
    contas_corrente = []

    # ---------------------------Laco de repeticao que chama as funcoes
    if False:
        while True:

            opcao = input(menu)

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))

                saldo, extrato = deposito(valor, saldo, extrato)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato, numero_saques = saque(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
                
            elif opcao == "e":
                func_extrato(saldo, extrato=extrato)

            elif opcao == "q":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    menu_inicial = '''

    [1] - Cadastrar cliente
    [2] - Criar conta corrente
    [3] - Sair
    
    -> 
    '''
    while True:
        opcoes = input(menu_inicial)
        if opcoes == '1':
           clientes.append(criar_usuario(clientes))
        elif opcoes == '2':
           contas_corrente.append(criar_conta_corrente(numero_de_contas))
        elif opcoes == '3':
            break
    print(f'Clientes -> \n{clientes} \n\n')
    print(f'contas corrente -> \n{contas_corrente}')
