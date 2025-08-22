from models.restaurante import Restaurante

restaurante1 = Restaurante('Japa food', 'praca da silva')
restaurante1.alternar_estado()
restaurante2 = Restaurante('caldo da jojo', 'praca joao de deus')
# restaurante2.alternar_estado()

#adicionando as notas
restaurante1.receber_avaliacao('Usuario1', 8)
restaurante1.receber_avaliacao('Usuario2', 5)

restaurante2.receber_avaliacao('Usuario3', 7)
restaurante2.receber_avaliacao('Usuario4', 3)

def main():
    Restaurante.lista_restaurante()

if __name__ == "__main__":
    main()
