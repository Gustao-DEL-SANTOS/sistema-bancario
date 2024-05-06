
def menu():
    op = '''
    =========== MENU =============
    
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar cliente
    [5] - Criar conta corrente
    [0] - Sair

'''
    return input(op)

def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
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
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")


def func_extrato(saldo, /, *, extrato):    
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n==========================================")


# Funcoes relacionadas ao usuario

def criar_usuario(clientes):
    cpf = input('CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, clientes)
    
    
    if usuario:
        print('CPF ja esta cadastrado...')
        print('Cadastre outro CPF...')
    else:
        nome = input('Nome: ')
        data_nascimento = input('Data de nascimento: (dd-mm-aaaa)')
        logradouro = input('Logradouro: ')
        numero_casa = input('Numero da Casa: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado Sigla (ex: SP): ')
        endereco = f'{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}'
        cli = dict(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        clientes.append(cli)
        print(cli)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None
    
def criar_conta_corrente(numero_conta_anterior):
    cliente = input('Cpf: ')
    numero_da_conta = numero_conta_anterior +1
    numero_agencia = '0001'
    return dict( numero_agencia=numero_agencia, numero_da_conta=numero_da_conta, cliente=cliente)

def listar_contas():
    pass


# -------------------------- DADOS DO BANCO E VARIAVEIS
if __name__ == "__main__":

    saldo = 50
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    numero_de_contas = 0 # numero das contas do banco

    clientes = []
    contas_corrente = []

# ---------------------------Laco de repeticao que chama as funcoes
    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
            
        elif opcao == "3":
            func_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(clientes)
        elif opcao == "5":
            contas_corrente.append(criar_conta_corrente(numero_de_contas))
        elif opcao == "6":
            listar_contas(contas_corrente)

        elif opcao == "0":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    
