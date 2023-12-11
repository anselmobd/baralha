from pprint import pprint
from random import randint

from baralla.tipo_baralho import TipoBaralho
from baralla.carta import Carta


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
            Carta(nf, n)
            for n in self.tipo_baralho.naipes
            for nf in self.tipo_baralho.numeros_figuras
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

    def get_str_monte(self):
        return "-".join([str(carta) for carta in self.monte])
