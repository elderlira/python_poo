class Cliente():

    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def imprimir_dados(self):
        print(f"Cliente: {self._nome} mora em {self._endereco}")
        return True