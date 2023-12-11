from pprint import pprint

from baralla.tipo_jogo import TipoJogo
from baralla.baralho import Baralho
from baralla.grupo import Grupo
from baralla.mesa import Mesa


class Partida:

    def __init__(self, tipo_jogo=None, grupo:Grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo

        self.caracteristicas = TipoJogo(tipo_jogo).caracteristicas
        self.baralho = Baralho(self.caracteristicas['baralho'])
        self.mesa = Mesa()

    def inicia(self):
        self.prepara()
        self.ciclo()
        self.print_estado()

    def prepara(self):
        self.grupo.set_tipo_jogo(self.tipo_jogo)
        self.baralho.embaralha()
        self.distribui()
        self.define_trunfo()
        self.mesa.set_baralho(self.baralho)

    def distribui(self):
        for _ in range(self.grupo.num_jogadores):
            jogador = self.grupo.get_jogador
            for _ in range(self.caracteristicas['preparação da partida']['parâmetros']['num_cartas']):
                carta = self.baralho.pega_carta()
                jogador.recebe_carta(carta)
            self.grupo.proximo()

    def define_trunfo(self):
        carta = self.baralho.pega_carta()
        self.baralho.coloca_carta_embaixo_monte(carta)
        self.mesa.set_trunfo(carta)

    def ciclo(self):
        self.grupo.todos_jogam(self.mesa)

    def print_estado(self):
        print('monte', self.baralho.get_str_monte())
        print('grupo', self.grupo.str_estado())
        print('mesa', repr(self.mesa))
