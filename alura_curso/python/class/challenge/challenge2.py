# Exercícios
# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
# Inicie um atributo chamado disponivel como True por padrão.
# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
# Crie duas instâncias da classe Livro e imprima essas instâncias.
# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e 
# retorna uma lista dos livros disponíveis publicados nesse ano.

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis 
# publicados em um ano específico.

# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, 
# instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

class Livros:
    livros_disponiveis = {}
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self.livros_disponiveis[ano_publicacao] = {'titulo': titulo.title(), 'autor': autor.title(), 'disponibilidade': self._disponivel}

    def __str__(self):
        return f"Titulo: {self._titulo}, Autor: {self._autor} e Ano: {self._ano_publicacao}"
    
    def emprestar(self):
        self._disponivel = False
        return(f"O livro {self._titulo} do autor {self._autor} não está disponível para emprestimo")
    
    @classmethod
    def verificar_disponibilidade(cls, ano):
        
        for disponivel in cls.livros_disponiveis:
            if disponivel == ano:
                return f"""
                O livro de titulo {cls.livros_disponiveis[ano]['titulo']}
                e ano {disponivel} esta disponivel
                """

            
            return f"Livro nao encontrado"


livro1 = Livros("a hora da estrela", "clarice linspector", 1980)
disponivel = livro1.emprestar()
# print(disponivel)
# print(Livros.livros_disponiveis)
verificar_disponibilidade = Livros.verificar_disponibilidade(1980)
print(verificar_disponibilidade)

