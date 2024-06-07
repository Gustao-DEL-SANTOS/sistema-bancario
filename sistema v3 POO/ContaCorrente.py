from Conta import Conta
from Saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
            if transacao['tipo'] == Saque.__name__]
        )
    
        excedeu_limite = valor >self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Você excedeu o limite de saques. @@@")
        else:
            return super().sacar(valor)
        
        return False

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} : ({self.agencia}, {self.numero}, {self.cliente.nome})>'

    def __str__(self):
        return f'''
    Agencia:\t{self.agencia}
    C/C:\t{self.numero}
    Titular:\t{self.cliente.nome}
    '''