from pprint import pprint

from baralla.carta import Carta
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

    def regua_de_cartas_ganhadoras_da_mao(self, carro, trumfo):
        result = []
        regua_valor = self.definicao['partida']['regua de valor dos números das cartas da mesa']
        for nf in regua_valor:
            result.append(Carta(naipe=carro, numero=nf))
        if carro != trumfo:
            for nf in regua_valor:
                result.append(Carta(naipe=trumfo, numero=nf))
        return result

    def define_vencedor_da_mao(self, mesa):
        regua = self.regua_de_cartas_ganhadoras_da_mao(
            mesa.cartas[0]['carta'].naipe,
            mesa.trunfo.naipe,
        )
        vencedor_pontos = -1
        vencedor_nome = ''
        for carta_jogador in mesa.cartas:
            try:
                valor = regua.index(carta_jogador['carta'])
            except ValueError:
                valor = -1
            if vencedor_pontos < valor:
                vencedor_pontos = valor
                vencedor_nome = carta_jogador['jogador']
        return vencedor_nome
