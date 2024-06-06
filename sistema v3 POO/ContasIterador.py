class ContasIterador:
    def __init__(self, contas):
        self._contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self._contas[self._index]
            return f'''
Agencia:\t{conta.agencia}
C/C:\t\t{conta.numero}
Titular:\t{conta.cliente.nome}
Saldo:\t\tR$ {conta.saldo:.2f}
                    '''
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1
