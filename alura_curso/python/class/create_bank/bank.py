class Conta:
    _quantidade = 0

    def __init__(self, numero: int):
        self._numero:int = numero
        self._saldo = 0.0
        self.adicionar_conta()

    def depositar(self,valor):
        self._saldo += valor
        print(f"voce acabou de depositar {valor}")

    def sacar(self, valor):
        if self._saldo <= valor:
            print(f"valor indisponivel para sacar")
            return False
        print(f"Voce sacou {valor}")

    def saldo(self):
        print(f"seu saldo é {self._saldo}")
        return self._saldo
    
    @classmethod
    def adicionar_conta(cls):
        cls._quantidade += 1
        print(f"Ja temos o total de {cls._quantidade} contas criadas")
        return cls._quantidade
    
    @classmethod
    def quantidade_contas_criadas(cls):
        print(cls._quantidade)
        return cls._quantidade

    
# conta1 = Conta(1111)
# conta1.depositar(500)
# conta1.saldo()
# conta1 = Conta.quantidade_contas_criadas()