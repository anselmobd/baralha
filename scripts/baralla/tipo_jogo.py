from pprint import pprint

from baralla.custom.tipo_jogo import CustomTipoJogo


class TipoJogo(CustomTipoJogo):

    def __init__(self, tipo=None) -> None:
        self.tipo = tipo if tipo else self.TESTE

    @property
    def definicao(self):
        return self._JOGOS[self.tipo]
