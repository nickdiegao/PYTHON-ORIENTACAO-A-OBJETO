from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import item_cardapio

class Restaurante:
    restaurantes = []

    def __init__(this, nome, categoria):
        this._nome = nome.title() #primeira letra maiúscula
        this._categoria = categoria.upper() #toda a palvara maiúscula
        this._ativo = False
        this._avaliacao = []
        this._cardapio = []
        Restaurante.restaurantes.append(this)

    def __str__(this):
        return f'{this.nome} | {this.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(this, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            this._avaliacao.append(avaliacao)
        

    @property
    def media_avaliacoes(this):
        if not this._avaliacao:
            return 'Sem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in this._avaliacao)
        quantidade_de_notas = len(this._avaliacao)

        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media

    def adicionar_ao_cardapio(self,item):
        if isinstance(item, item_cardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)