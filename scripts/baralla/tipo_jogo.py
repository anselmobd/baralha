from pprint import pprint

from baralla.custom.tipo_jogo import CustomTipoJogo


class TipoJogo(CustomTipoJogo):

    def __init__(self, id=None) -> None:
        self._id = id if id else self.TESTE

    @property
    def id(self):
        return self._id

    @property
    def definicao(self):
        return self._JOGOS[self._id]
