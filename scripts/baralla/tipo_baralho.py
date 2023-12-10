from pprint import pprint

from baralla.custom.tipo_baralho import CustomTipoBaralho


class TipoBaralho(CustomTipoBaralho):

    def __init__(self, tipo=None) -> None:
        self.tipo = tipo if tipo else self.TESTE

    @property
    def naipes(self):
        return self._NAIPE[self.tipo]

    @property
    def numeros_figuras(self):
        return self._NUMERO_FIGURA[self.tipo]
