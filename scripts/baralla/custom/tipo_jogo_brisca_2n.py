from pprint import pprint

from baralla.tipo_baralho import TipoBaralho
from baralla.custom.tipo_jogo_brisca import TipoJogoBrisca


class TipoJogoBrisca2Naipes:
    ID = 'brisca2n'
    DEFINICAO = TipoJogoBrisca.DEFINICAO
    DEFINICAO['baralho'] = TipoBaralho.ESPANHOL2N
