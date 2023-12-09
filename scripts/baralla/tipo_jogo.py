from pprint import pprint

from baralla.custom.tipo_jogo import CustomTipoJogo


class TipoJogo(CustomTipoJogo):
    pass

    def caracteristicas(self, tipo):
        return self._JOGOS[tipo]
