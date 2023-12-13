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

    def minha_carta_melhor_que_a_da_mesa(self, mesa, mao):
        regua_valor = self.jogo_def['partida']['regua de valor dos números das cartas da mesa']
        mesa_naipe = mesa.cartas[0]['carta'].naipe
        mesa_numero = mesa.cartas[0]['carta'].numero
        mesa_valor = regua_valor.index(mesa_numero)
        carta_idx = -1
        carta_melhor_valor = -1
        for idx, carta in enumerate(mao):
            if carta.naipe == mesa_naipe:
                carta_valor = regua_valor.index(carta.numero)
                if carta_valor > mesa_valor and carta_valor > carta_melhor_valor:
                    carta_melhor_valor = carta_valor
                    carta_idx = idx
        return carta_idx


    def v0_11_0(self, mesa, mao):
        """
        Como primeiro: sorteia uma carta
        Como segundo: escolhe carta maior que a da mesa, se tiver, senão sorteia
        """
        if mesa.cartas:
            idx = self.minha_carta_melhor_que_a_da_mesa(self, mesa, mao)
            if idx > -1:
                return idx
        return self.v0_10_0(mesa, mao)
