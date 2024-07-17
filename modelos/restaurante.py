from statistics import mean
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    # _variable = protetected (Class and subclasses (inheritance))
    # __variable = private

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Getter for the ativo attribute"""
        return '☒' if self._ativo else '☐'

    @ativo.setter
    def ativo(self, ativo):
        """Setter for the ativo attribute"""
        self._ativo = ativo

    # @ativo.deleter
    # def ativo(self):
    #     del self._ativo


    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0

        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)
        return media

    @property
    def media_avaliacoes_2(self):
        if not self._avaliacao:
            return 0

        #Roda a função em cima da lista, transformando numa lista de numeros
        notas = list(map(lambda x: x._nota, self._avaliacao))
        return round(mean(notas), 1)
