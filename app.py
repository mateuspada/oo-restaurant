from modelos.restaurante import Restaurante

restaurante_praca = Restaurante(nome='praça', categoria='Gourmet')
restaurante_praca.receber_avaliacao('Gui', 3)
restaurante_praca.receber_avaliacao('Lais', 0)
restaurante_praca.receber_avaliacao('Emy', 2)
# restaurante_mexicano = Restaurante(nome='mexican food', categoria='Mexicana')
# restaurante_japones = Restaurante(nome='japa', categoria='Japonesa')

# restaurante_mexicano.ativo = True
# del restaurante_mexicano.ativo


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
