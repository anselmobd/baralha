from pprint import pprint
from random import randint

from baralla.logica import Logica


class Jogador:

    def __init__(self, nome, logica='0.10.0') -> None:
        self.nome = nome

        self.logica = logica
        self.logica_executa = Logica(logica).executa

        self.tipo_jogo = None
        self.jogo_def = None
        self.partidas = 0
        self.prepara()

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:
        return f"Jogador({self.nome})"

    def prepara(self):
        self._mao = []
        self.monte = []
        self.valor_no_monte = 0

    def recebe_carta(self, carta):
        self._mao.append(carta)

    @property
    def mao(self):
        return self._mao

    @property
    def tem_carta(self):
        return len(self._mao) != 0

    def inicia_tipo_jogo(self, tipo_jogo):
        self.tipo_jogo = tipo_jogo
        self.jogo_def = self.tipo_jogo.definicao
        self.partidas = 0

    def joga(self, mesa):
        """Aqui entrará a lógica de decisão do jogador"""
        carta_idx = self.logica_executa(mesa, self.mao)
        mesa.coloca_carta(self.mao.pop(carta_idx), self)

    def recolhe_mesa(self, mesa) -> None:
        pontos = self.jogo_def['pontos no jogo']['pontos das cartas']
        while mesa.cartas:
            carta_jogador = mesa.cartas.pop()
            self.monte.append(carta_jogador['carta'])
            self.valor_no_monte += pontos.get(carta_jogador['carta'].numero, 0)
