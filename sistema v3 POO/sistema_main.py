from Conta import Conta
from Cliente import Cliente
from Deposito import Deposito
from Saque import Saque
from Historico import Historico
from ContaCorrente import ContaCorrente
from PessoaFisica import PessoaFisica
from Transacao import Transacao



def menu():
    op = '''
    =========== MENU =============
    
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar cliente
    [5] - Criar conta corrente
    [6] - listar contas
    [0] - Sair
    
    => '''
    return input(op)



def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf ==cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\n@@@ Cliente nao possui conta ! @@@')
        return
    return cliente.contas[0]
    


def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado... @@@')
        return

    valor = float(input('Informe o valor do deposito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)



def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado... @@@')
        return
    
    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)



def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não encontrado... @@@')
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print('\n==================== EXTRATO ====================')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Nao foram realizadas movimentacoes...'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']} :\n\t R$ {transacao['valor']:.2f}'
    
    print(extrato)
    print(f'\nSaldo:\n\t{conta.saldo:.2f}')
    print('===================================================')



def criar_cliente(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\n@@@ Cliente ja cadastrado... @@@')
        return

    nome = input('Nome: ')
    data_nascimento = input('Data de nascimento: (dd-mm-aaaa)')
    logradouro = input('Logradouro: ')
    numero_casa = input('Numero da Casa: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado Sigla (ex: SP): ')
    endereco = f'{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}'
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print('\n=== cliente criado com sucesso! ===')



def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ cliente nao encontrado, fluxo de criação encerrado! @@@')
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\n=== Conta criada com sucesso! ===')



def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(str(conta))


clientes = []
contas = []

# ---------------------------Laco de repeticao que chama as funcoes
while True:

    opcao = menu()

    if opcao == "1":
        depositar(clientes)

    elif opcao == "2":
        sacar(clientes)

    elif opcao == "3":
        exibir_extrato(clientes)

    elif opcao == "4":
        criar_cliente(clientes)

    elif opcao == "5":
        numero_conta = len(contas) +1
        criar_conta(numero_conta, clientes, contas)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
