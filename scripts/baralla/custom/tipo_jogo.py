from pprint import pprint

from baralla.tipo_baralho import TipoBaralho
from baralla.custom.tipo_jogo_brisca import TipoJogoBrisca
from baralla.custom.tipo_jogo_brisca_2n import TipoJogoBrisca2Naipes
from baralla.custom.tipo_jogo_teste import TipoJogoTeste


class CustomTipoJogo:

    def __init__(self) -> None:
        self.jogos = {}
        self.default = None

        self.adiciona(TipoJogoTeste)
        self.adiciona(TipoJogoBrisca)
        self.adiciona(TipoJogoBrisca2Naipes)

    def adiciona(self, TipoJogo) -> None:
        self.jogos[TipoJogo.ID] = TipoJogo.DEFINICAO
        if not self.default:
            self.default = TipoJogo.ID
