# Exercícios
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
# Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. 
# Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria.
# Exiba essa mensagem para uma instância de restaurante.
# Crie uma classe chamada Cliente e pense em 4 atributos. 
# Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Carro:

    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo.title()
        self.cor = cor.title()
        self.ano = ano

carro1 = Carro("Fiesta", "prata", 2013)

class Restaurante:
    def __init__(self, nome, categoria, local, atendimento_online, ativo=False):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self.ativo = ativo
        self.local = local.title()
        self.atendimento_online = atendimento_online

    def __str__(self):
        return f"O restaurante {self.nome} é do tipo {self.categoria}"

pizzaria = Restaurante(nome = 'noustra pizza', categoria='pizzaria italiana', local='Praca nossa senhora da luz',atendimento_online='Nao' ,ativo=True)
print(pizzaria)



