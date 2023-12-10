from pprint import pprint

from baralla.tipo_jogo import TipoJogo
from baralla.baralho import Baralho
from baralla.grupo import Grupo
from baralla.mesa import Mesa


class Jogo:

    def __init__(self, tipo_jogo=None, grupo:Grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo

        self.caracteristicas = TipoJogo(tipo_jogo).caracteristicas
        self.baralho = Baralho(self.caracteristicas['baralho'])
        self.mesa = Mesa()

    def inicia(self):
        self.prepara()
        self.ciclo()

    def prepara(self):
        print("preparando o jogo")
        self.grupo.set_tipo_jogo(self.tipo_jogo)
        self.baralho.embaralha()
        self.distribui()
        self.define_trumfo()
        self.mesa.set_baralho(self.baralho)

    def distribui(self):
        for _ in range(self.grupo.num_jogadores):
            jogador = self.grupo.get_jogador
            print('cartas para', jogador)
            for _ in range(self.caracteristicas['preparação do jogo']['parâmetros']['num_cartas']):
                carta = self.baralho.get_carta()
                jogador.recebe_carta(carta)
            pprint(jogador.mao)
            self.grupo.proximo()

    def define_trumfo(self):
        carta = self.baralho.see_carta()
        self.mesa.set_trumfo(carta)

    def ciclo(self):
        print("iniciando ciclo")
        self.grupo.todos_jogam(self.mesa)
        print(repr(self.mesa))
