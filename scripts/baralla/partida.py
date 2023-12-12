from pprint import pprint

from baralla.baralho import Baralho
from baralla.grupo import Grupo
from baralla.jogador import Jogador
from baralla.mesa import Mesa
from baralla.tipo_jogo import TipoJogo


class Partida:

    def __init__(self, tipo_jogo:TipoJogo=None, grupo:Grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo

        self.baralho = Baralho(self.tipo_jogo.definicao['baralho'])
        self.mesa = Mesa()

    def inicia(self):
        self.prepara()
        self.ciclo()
        self.finaliza()

    def prepara(self):
        self.grupo.prepara()
        self.baralho.embaralha()
        self.distribui()
        self.define_trunfo()
        self.print_preparado()

    def distribui(self):
        for _ in range(self.grupo.num_jogadores):
            jogador = self.grupo.get_jogador
            for _ in range(self.tipo_jogo.definicao['preparação da partida']['parâmetros']['num_cartas']):
                carta = self.baralho.pega_carta()
                jogador.recebe_carta(carta)
            self.grupo.proximo()

    def define_trunfo(self):
        carta = self.baralho.pega_carta()
        self.baralho.carta_volta_para_baixo_do_monte(carta)
        self.mesa.set_trunfo(carta)

    def ciclo(self):
        while self.grupo.tem_cartas:
            self.print_monte_maos()
            self.grupo.todos_jogam(self.mesa)
            self.print_mesa()
            vencedor : Jogador = self.tipo_jogo.define_vencedor_da_mao(self.mesa)
            print('vencedor da mão', vencedor)
            vencedor.recolhe_mesa(self.mesa)
            self.grupo.define_proximo_jogador(vencedor)
            self.grupo.todos_compram(self.baralho)

    def print_preparado(self):
        pprint({
            'baralho': self.baralho,
            'trunfo': self.mesa.trunfo,
        })

    def print_monte_maos(self):
        print('monte', self.baralho.get_str_monte())
        print('grupo mãos', self.grupo.str_maos())

    def print_mesa(self):
        print('mesa', repr(self.mesa))

    def finaliza(self):
        print('grupo montes', self.grupo.str_montes())
        vencedor : Jogador = self.grupo.define_vencedor_da_partida()
        print('vencedor da partida', vencedor)
