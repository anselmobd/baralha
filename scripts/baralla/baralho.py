from pprint import pprint
from random import randint

from baralla.tipo_baralho import TipoBaralho


class Baralho:

    def __init__(self, tipo=None) -> None:
        self.tipo_baralho = TipoBaralho(tipo)
        self.cria_baralho()

        self.monte = []
        self.descarte = []
        self.ordena()
        
    def __repr__(self):
        tipo = self.tipo_baralho.tipo
        tam_baralho = len(self.baralho)
        tam_monte = len(self.monte)
        tam_decarte = len(self.descarte)
        return repr(f"Baralho {tipo} de {tam_baralho} cartas, {tam_monte} no monte e {tam_decarte} fora")

    def embaralha(self):
        self.monte = []
        temporario = self.baralho.copy()
        while temporario:
            carta_idx = randint(0, len(temporario)-1)
            carta = temporario[carta_idx]
            self.monte.append(carta)
            del(temporario[carta_idx])

    def ordena(self):
        self.monte = self.baralho.copy()

    def cria_baralho(self):
        self.baralho = [
            (c, n)
            for n in self.tipo_baralho.naipes
            for c in self.tipo_baralho.cartas
        ]
    
    def pega_carta(self):
        carta_idx = 0
        carta = self.monte[carta_idx]
        self.descarte.append(carta)
        del(self.monte[carta_idx])
        return carta

    def coloca_carta_embaixo_monte(self, carta):
        self.descarte = [
            fica for fica in self.descarte
            if fica != carta
        ]
        self.monte.append(carta)

    def ve_carta(self, position=None):
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
