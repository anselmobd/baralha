from pprint import pprint
from random import randint


class Logica:

    def __init__(self, jogo_def, versao) -> None:
        self.jogo_def = jogo_def
        self.versao = versao
        self.VERSOES = {
            '0.10.0': self.v0_10_0,
            '0.10.1': self.v0_10_1,
            '0.11.0': self.v0_11_0,
        }

    def executa(self, mesa, mao):
        return self.VERSOES[self.versao](mesa, mao)

    def v0_10_0(self, mesa, mao):
        """Sorteia uma carta"""
        return randint(0, len(mao)-1)

    def v0_10_1(self, mesa, mao):
        """Pega a primeira carta recebida"""
        return 0

    def v0_11_0(self, mesa, mao):
        """
        Como primeiro: sorteia uma carta
        Como segundo: escolhe carta maior que a da mesa, se tiver, senão sorteia
        """
        # print('v0_11_0')
        pontos = self.jogo_def['pontos no jogo']['pontos das cartas']
        regua_valor = self.jogo_def['partida']['regua de valor dos números das cartas da mesa']
        if mesa.cartas:
            # pprint(mesa)
            # pprint(mesa.cartas[0])
            naipe = mesa.cartas[0]['carta'].naipe
            numero = mesa.cartas[0]['carta'].numero
            # print(numero, naipe)
            # print(pontos.get(numero, 0))
            # pprint(regua_valor)
            valor_numero = regua_valor.index(numero)
            # print(valor_numero)
            # pprint(mao)
            melhor_idx = -1
            melhor_valor = -1
            for idx, carta in enumerate(mao):
                # print(carta.numero, carta.naipe)
                if carta.naipe == naipe:
                    carta_valor = regua_valor.index(carta.numero)
                    if carta_valor > valor_numero and carta_valor > melhor_valor:
                        melhor_valor = carta_valor
                        melhor_idx = idx
            # print('melhor_idx', melhor_idx, mao[melhor_idx])
            if melhor_idx > -1:
                return melhor_idx
        # print('sem mesa')
        return self.v0_10_0(mesa, mao)
