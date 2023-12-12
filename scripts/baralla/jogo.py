from pprint import pprint
from random import seed, randint

from baralla.partida import Partida
from baralla.tipo_jogo import TipoJogo


class Jogo:
    
    def __init__(self, tipo_jogo=None, grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo

        self.jogo_def = TipoJogo(tipo_jogo).definicao

    def iniciar(self):
        self.grupo.sorteia()
        for _ in range(self.jogo_def['jogo']['num_partidas']):
            jogo = Partida(self.tipo_jogo, self.grupo)
            jogo.inicia()
