from pprint import pprint
from random import seed, randint

from baralla.partida import Partida
from baralla.tipo_jogo import TipoJogo


class Jogo:
    
    def __init__(self, tipo_jogo_id=None, grupo=None) -> None:
        self.tipo_jogo_id = tipo_jogo_id
        self.grupo = grupo

        self.tipo_jogo = TipoJogo(self.tipo_jogo_id)
        self.tipo_jogo_id = self.tipo_jogo.id
        self.jogo_def = self.tipo_jogo.definicao

    def iniciar(self):
        self.grupo.sorteia()
        for _ in range(self.jogo_def['jogo']['num_partidas']):
            jogo = Partida(self.tipo_jogo, self.grupo)
            jogo.inicia()
