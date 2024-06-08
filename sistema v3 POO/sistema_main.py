from datetime import datetime
from pathlib import Path

from ContaCorrente import ContaCorrente
from ContasIterador import ContasIterador
from Deposito import Deposito
from PessoaFisica import PessoaFisica
from Saque import Saque

ROOT_PATH = Path(__file__).parent


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        # print(f'{datetime.utcnow()}: {func.__name__.upper()}')
        with open(ROOT_PATH / 'log.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(
                f'[{datetime.now()}] Funcao {func.__name__.upper()} executada com argumentos {args} e ' +
                '{kwargs}. Retornou {resultado} \n'
            )

        return resultado
    return envelope


def menu():
    op = '''=========== MENU =============\n
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar cliente
    [5] - Criar conta corrente
    [6] - listar contas
    [0] - Sair\n
    => '''
    return input(op)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\n@@@ Cliente nao possui conta ! @@@')
        return
    return cliente.contas[0]


@log_transacao
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


@log_transacao
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


@log_transacao
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

    extrato = ''
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao='saque'):
        extrato += f'\n{transacao['data']}\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}\n'
        tem_transacao = True

    for transacao in conta.historico.gerar_relatorio(tipo_transacao='deposito'):
        extrato += f'\n{transacao['data']}\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}\n'
        tem_transacao = True

    if not tem_transacao:
        extrato = 'Nao foram realizadas movimentacoes...'

    print(extrato)
    print(f'\nSaldo:\n\t{conta.saldo:.2f}\n')
    print('==================================================')


@log_transacao
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


@log_transacao
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
    for conta in ContasIterador(contas):
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
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
