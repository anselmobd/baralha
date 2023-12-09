from pprint import pprint

from baralla.tipo_jogo import TipoJogo
from baralla.baralho import Baralho
from baralla.jogador import Grupo


class Jogo:

    def __init__(self, tipo_jogo=None, grupo:Grupo=None) -> None:
        self.tipo_jogo = tipo_jogo
        self.grupo = grupo

        self.caracteristicas = TipoJogo(tipo_jogo).caracteristicas
        self.baralho = Baralho(self.caracteristicas['baralho'])

    def inicia(self):
        self.prepara()

    def prepara(self):
        print("preparando o jogo")
        self.baralho.embaralha()
        for _ in range(self.grupo.num_jogadores):
            jogador = self.grupo.get_jogador
            print(jogador.nome)
            self.grupo.proximo()
