from pprint import pprint
from random import seed, randint

from baralla.jogo import Jogo
from baralla.tipo_jogo import TipoJogo


class Partida:
    
    def __init__(self, tipo_jogo=TipoJogo.TESTE, grupo=None) -> None:
        self.carac_jogo = TipoJogo().caracteristicas(tipo_jogo)
        self.grupo = grupo

    def iniciar(self):
        for idx_jogo in range(self.carac_jogo['partida']['num_jogos']):
            jogo = Jogo(self.carac_jogo)
            jogo.iniciar()
