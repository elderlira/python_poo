# Agora é sua vez! 
# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:

    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return (f"Ola {self.pessoa}, voce tem {self.idade} anos e atualmente exerce a profissao de {self._profissao}")
    

    def aniversario(self):
        self._idade += 1

    
    @property
    def saudacao(self):
        return print(f"Parabens por sua profissao de {self._profissao}. Voce é um excelente profissional")



