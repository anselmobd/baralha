from pprint import pprint

from baralla.custom.tipo_baralho import CustomTipoBaralho


class TipoBaralho(CustomTipoBaralho):

    def __init__(self, tipo=None) -> None:
        self.tipo = tipo if tipo else self.TESTE

    @property
    def naipes(self):
        return self._NAIPES[self.tipo]

    @property
    def cartas(self):
        return self._CARTAS[self.tipo]
