from pprint import pprint, pformat
from random import randint

from baralla.jogador import Jogador


class Grupo:

    def __init__(self) -> None:
        self.jogadores : dict[int, Jogador] = {}
        self.idx_da_vez : int = 0

    def __repr__(self) -> str:
        return pformat({
            self.jogadores[idx]: self.jogadores[idx].logica
            for idx in self.jogadores
        })

    @property
    def num_jogadores(self) -> int:
        return len(self.jogadores)

    @property
    def da_vez(self) -> Jogador:
        return self.jogadores.get(self.idx_da_vez, None)

    @property
    def get_jogador(self) -> Jogador:
        return self.jogadores[self.idx_da_vez]

    def adiciona(self, jogador:Jogador) -> None:
        self.jogadores[self.num_jogadores] = jogador

    def sorteia(self) -> None:
        self.idx_da_vez = randint(0, self.num_jogadores - 1)

    def proximo(self) -> None:
        self.idx_da_vez = (self.idx_da_vez + 1) % self.num_jogadores

    def define_proximo_jogador(self, jogador:Jogador) -> None:
        for idx_jogador in self.jogadores:
            if self.jogadores[idx_jogador] == jogador:
                self.idx_da_vez = idx_jogador

    def inicia_tipo_jogo(self, tipo_jogo) -> None:
        for idx_jogador in self.jogadores:
            self.jogadores[idx_jogador].inicia_tipo_jogo(tipo_jogo)

    def placar(self) -> dict[Jogador, int]:
        result = {}
        for idx_jogador in self.jogadores:
            result[self.jogadores[idx_jogador]] = self.jogadores[idx_jogador].partidas 
        return result

    def todos_jogam(self, mesa) -> None:
        for _ in self.jogadores:
            self.jogadores[self.idx_da_vez].joga(mesa)
            self.proximo()

    def todos_compram(self, baralho) -> None:
        for _ in self.jogadores:
            carta = baralho.pega_carta()
            if carta:
                self.jogadores[self.idx_da_vez].recebe_carta(carta)
            self.proximo()

    @property
    def tem_cartas(self) -> bool:
        for _ in self.jogadores:
            if self.jogadores[self.idx_da_vez].tem_carta:
                return True
        return False

    def str_maos(self) -> dict[Jogador, list]:
        return {
            self.jogadores[jogador].nome: self.jogadores[jogador].mao
            for jogador in self.jogadores
        }

    def str_montes(self) -> dict[str, tuple]:
        return {
            self.jogadores[jogador].nome: (
                self.jogadores[jogador].monte,
                self.jogadores[jogador].valor_no_monte,
            )
            for jogador in self.jogadores
        }

    def prepara(self) -> None:
        for jogador in self.jogadores:
            self.jogadores[jogador].prepara()

    def define_vencedor_da_partida(self) -> Jogador:
        vencedor_pontos = -1
        vencedor = None
        for jogador in self.jogadores:
            valor = self.jogadores[jogador].valor_no_monte
            if vencedor_pontos < valor:
                vencedor_pontos = valor
                vencedor = self.jogadores[jogador]
        return vencedor
