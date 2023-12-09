from pprint import pprint

from baralla.tipo_jogo import TipoJogo


class Jogo:

    def __init__(self, tipo_jogo=None) -> None:
        self.tipo_jogo = tipo_jogo

        self.caracteristicas = TipoJogo(tipo_jogo).caracteristicas


    def iniciar(self):
        print("iniciando jogo")
