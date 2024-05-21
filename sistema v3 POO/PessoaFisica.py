from Cliente import Cliente
class PessoaFisica(Cliente):
    def __iniT__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf