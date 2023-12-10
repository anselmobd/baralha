from pprint import pprint
from random import randint

from baralla.tipo_baralho import TipoBaralho


class Baralho:

    __ALEATORIA = 'aleatória'
    __ORDENADA = 'ordenada'

    def __init__(self, tipo=None) -> None:
        self.tipo_baralho = TipoBaralho(tipo)

        self.exclui_baralho()
        self.ordena()
        
    def __repr__(self):
        tipo = self.tipo_baralho.tipo
        tam_monte = len(self.monte)
        tam_decarte = len(self.descarte)
        return repr(f"Baralho {tipo}; {tam_monte} cartas no monte, {tam_decarte} fora")

    def embaralha(self):
        self.ordem = self.__ALEATORIA
        self.inicializa_baralho()

    def ordena(self):
        self.ordem = self.__ORDENADA
        self.inicializa_baralho()

    def exclui_baralho(self):
        self.monte = []
        self.descarte = []
    
    def inicializa_baralho(self):
        self.exclui_baralho()
        self.monte = [
            (c, n)
            for n in self.tipo_baralho.naipes
            for c in self.tipo_baralho.cartas
        ]
    
    def get_carta(self):
        carta_idx = 0 if self.ordem == self.__ORDENADA else randint(0, len(self.monte)-1)
        carta = self.monte[carta_idx]
        self.descarte.append(carta)
        del(self.monte[carta_idx])
        return carta

    def see_carta(self, position=None):
        carta_idx = position if position else len(self.monte)-1
        return self.monte[carta_idx]

    # metodos para verificar conteúdo de artributos

    def mostra_monte(self, n=0):
        self.mostra_cartas(self.monte, n)

    def mostra_descarte(self, n=0):
        self.mostra_cartas(self.descarte, n)

    def mostra_tudo(self, n=0):
        print('monte')
        self.mostra_cartas(self.monte, n)
        print('descarte')
        self.mostra_cartas(self.descarte, n)

    def get_cartas(self, cartas, n=0):
        result = []
        for i, carta in enumerate(cartas, start=1):
            result.append(carta)
            if i == n:
                break
        return result

    def mostra_cartas(self, cartas, n=0):
        for carta in self.get_cartas(cartas, n):
            pprint(carta)

    def str_tudo(self, n=0):
        print('monte', self.str_cartas(self.monte, n))
        print('descarte', self.str_cartas(self.descarte, n))

    def str_cartas(self, cartas, n=0):
        return "-".join(
            [f"{c}{n}" for c, n in self.get_cartas(cartas, n)]
        )
