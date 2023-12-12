from pprint import pprint
from random import randint

from baralla.jogador import Jogador


class Grupo:

    def __init__(self) -> None:
        self.jogadores = {}
        self._idx_da_vez = 0

    @property
    def num_jogadores(self):
        return len(self.jogadores)

    @property
    def da_vez(self):
        return self.jogadores.get(self._idx_da_vez, "")

    @property
    def idx_da_vez(self):
        return self._idx_da_vez

    @property
    def get_jogador(self) -> Jogador:
        return self.jogadores[self.idx_da_vez]

    def adiciona(self, jogador):
        self.jogadores[self.num_jogadores] = jogador

    def sorteia(self):
        self._idx_da_vez = randint(0, self.num_jogadores - 1)

    def proximo(self):
        self._idx_da_vez = (self._idx_da_vez + 1) % self.num_jogadores

    def define_proximo_jogador(self, jogador):
        for idx_jogador in self.jogadores:
            if self.jogadores[idx_jogador] == jogador:
                self._idx_da_vez = idx_jogador

    def set_tipo_jogo(self, tipo_jogo):
        for idx_jogador in self.jogadores:
            self.jogadores[idx_jogador].set_tipo_jogo(tipo_jogo)

    def todos_jogam(self, mesa):
        for _ in self.jogadores:
            self.jogadores[self.idx_da_vez].joga(mesa)
            self.proximo()

    def todos_compram(self, baralho):
        for _ in self.jogadores:
            carta = baralho.pega_carta()
            self.jogadores[self.idx_da_vez].recebe_carta(carta)
            self.proximo()

    @property
    def tem_cartas(self):
        for _ in self.jogadores:
            if self.jogadores[self.idx_da_vez].tem_carta:
                return True
        return False

    def str_maos(self):
        return {
            self.jogadores[jogador].nome: self.jogadores[jogador].mao
            for jogador in self.jogadores
        }

    def str_montes(self):
        return {
            self.jogadores[jogador].nome: (
                self.jogadores[jogador].monte,
                self.jogadores[jogador].valor_no_monte,
            )
            for jogador in self.jogadores
        }

    def define_vencedor_da_partida(self):
        vencedor_pontos = -1
        vencedor = None
        for jogador in self.jogadores:
            valor = self.jogadores[jogador].valor_no_monte
            if vencedor_pontos < valor:
                vencedor_pontos = valor
                vencedor = self.jogadores[jogador]
        return vencedor
