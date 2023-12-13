from pprint import pprint
from random import randint


class Logica:

    def __init__(self, jogo_def, versao) -> None:
        self.jogo_def = jogo_def
        self.versao = versao
        self.VERSOES = {
            '0.10.0': self.v0_10_0,
            '0.10.1': self.v0_10_1,
        }

    def executa(self, mesa, mao):
        return self.VERSOES[self.versao](mesa, mao)

    def v0_10_0(self, mesa, mao):
        """Sorteia uma carta"""
        return randint(0, len(mao)-1)

    def v0_10_1(self, mesa, mao):
        """Pega a primeira carta recebida"""
        return 0
