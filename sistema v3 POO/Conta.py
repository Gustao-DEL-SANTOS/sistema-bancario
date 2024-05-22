from Historico import Historico
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor:float):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\n@@@ Operacao falhou! Voce nao tem saldo suficiente. @@@')
        elif valor > 0:
            self._saldo -= valor
            print('\n=== Saque realizado com sucesso! ===')
            return True
        else:
            print('\n@@@ Operacao falhou! O valor informado e invalido. @@@')
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n=== Deposito realizado com sucesso! ===')
        else:
            print('\n@@@ Operacao falhou! O valor informado e invalido. @@@')
            return False
        
        return True


    def __str__(self):
        return f'''
        Agencia:\t{self.agencia}
        C/C:\t{self.numero}
        Titular:\t{self.cliente.nome}
'''