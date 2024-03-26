from models.cardapio.item_cardapio import item_cardapio

class Bebida(item_cardapio):
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco)
        self.tamanho = tamanho
    
    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)