from pprint import pprint

from baralla.baralho import Baralho
from baralla.carta import Carta
from baralla.grupo import Grupo
from baralla.mesa import Mesa
from baralla.tipo_jogo import TipoJogo


class Partida:

    def __init__(self, tipo_jogo=None, grupo:Grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo


        self.baralho = Baralho(self.tipo_jogo.definicao['baralho'])
        self.mesa = Mesa()

    def inicia(self):
        self.prepara()
        self.ciclo()

    def prepara(self):
        self.grupo.set_tipo_jogo(self.tipo_jogo.id)
        self.baralho.embaralha()
        self.distribui()
        self.define_trunfo()
        self.mesa.set_baralho(self.baralho)

    def distribui(self):
        for _ in range(self.grupo.num_jogadores):
            jogador = self.grupo.get_jogador
            for _ in range(self.tipo_jogo.definicao['preparação da partida']['parâmetros']['num_cartas']):
                carta = self.baralho.pega_carta()
                jogador.recebe_carta(carta)
            self.grupo.proximo()

    def define_trunfo(self):
        carta = self.baralho.pega_carta()
        self.baralho.coloca_carta_embaixo_monte(carta)
        self.mesa.set_trunfo(carta)

    def ciclo(self):
        self.grupo.todos_jogam(self.mesa)
        vencedor_nome = self.define_vencedor()
        self.print_estado()
        print('vencedor_nome', vencedor_nome)

    def regua_de_cartas_ganhadoras(self, carro, trumfo):
        result = []
        regua_valor = self.tipo_jogo.definicao['partida']['regua de valor dos números das cartas da mesa']
        for nf in regua_valor:
            result.append(Carta(naipe=carro, numero=nf))
        if carro != trumfo:
            for nf in regua_valor:
                result.append(Carta(naipe=trumfo, numero=nf))
        return result

    def define_vencedor(self):
        regua = self.regua_de_cartas_ganhadoras(
            self.mesa.cartas[0]['carta'].naipe,
            self.mesa.trunfo.naipe,
        )
        vencedor_pontos = -1
        vencedor_nome = ''
        for carta_jogador in self.mesa.cartas:
            try:
                valor = regua.index(carta_jogador['carta'])
            except ValueError:
                valor = -1
            if vencedor_pontos < valor:
                vencedor_pontos = valor
                vencedor_nome = carta_jogador['jogador']
        return vencedor_nome

    def print_estado(self):
        print('monte', self.baralho.get_str_monte())
        print('grupo', self.grupo.str_estado())
        print('mesa', repr(self.mesa))
