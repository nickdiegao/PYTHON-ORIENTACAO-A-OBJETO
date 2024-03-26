from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_praca = Restaurante('praça','gourmet')
restaurante_mexicano = Restaurante('mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa','Japonesa')

restaurante_japones.alternar_estado()

restaurante_praca.receber_avaliacao('Nicholas', 2)
restaurante_praca.receber_avaliacao('Sheron', 3)
restaurante_japones.receber_avaliacao('Nicholas', 4)

bebida_suco = Bebida('Suco de abacaxi', 5.0, 'Grande')
prato_sushi = Prato('Sushi',40.0,'O melhor sushi da cidade')

bebida_suco.aplicar_desconto()
prato_sushi.aplicar_desconto()

restaurante_praca.adicionar_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_ao_cardapio(prato_sushi)

def main():
    # Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()