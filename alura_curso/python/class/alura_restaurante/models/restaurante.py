from models.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self._nome} e categoria {self._categoria}"
    
    @property
    def ativo(self):
        return  '✅' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo
       

    @classmethod
    def lista_restaurante(cls):
        print(f"{'Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)}|{'Status'.ljust(25)}")
        for restaurante in cls.restaurantes:
           print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao()).ljust(25)} | {restaurante.ativo}")
    
    def receber_avaliacao(self, cliente, nota):

        if nota > 5:
          nota -= 5
          return self._avaliacao.append(Avaliacao(cliente, nota))
        
        return self._avaliacao.append(Avaliacao(cliente, nota))
    
    def media_avaliacao(self):

        if not self._avaliacao:
            return 'Sem avaliação'
        
        soma_avaliacao = sum(soma_avaliacao._nota for soma_avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_avaliacao/quantidade_notas, 1)
        return media