from pprint import pprint
from random import seed, randint

from baralla.jogo import Jogo
from baralla.tipo_jogo import TipoJogo


class Partida:
    
    def __init__(self, tipo_jogo=None, grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo

        self.caracteristicas = TipoJogo(tipo_jogo).caracteristicas

    def iniciar(self):
        self.grupo.sorteia()
        for idx_jogo in range(self.caracteristicas['partida']['num_jogos']):
            jogo = Jogo(self.tipo_jogo, self.grupo)
            jogo.inicia()
