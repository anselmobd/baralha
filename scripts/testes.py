from pprint import pprint
from random import seed, randint

from baralla.baralho import Baralho
from baralla.jogador import Grupo, Jogador
from baralla.tipo_baralho import TipoBaralho
from baralla.tipo_jogo import TipoJogo


class Jogo:
    def __init__(self, carac_jogo) -> None:
        self.carac_jogo = carac_jogo
        self.grupo = None

    def iniciar(self):
        print("iniciando jogo")
        pass


class Partida:
    
    def __init__(self, tipo_jogo=TipoJogo.TESTE, grupo=None) -> None:
        self.carac_jogo = TipoJogo().caracteristicas(tipo_jogo)
        self.grupo = grupo

    def iniciar(self):
        for idx_jogo in range(self.carac_jogo['partida']['num_jogos']):
            jogo = Jogo(self.carac_jogo)
            jogo.iniciar()


def testa_baralho():
    baralho = Baralho(TipoBaralho.ESPANHOL)
    baralho.embaralha()
    
    baralho.str_tudo(5)
    while baralho.monte:
        baralho.vira_carta()
        baralho.str_tudo(5)


def monta_grupo_de_2():
    anselmo = Jogador('Anselmo')
    filha = Jogador('Filha')

    grupo = Grupo()
    grupo.adiciona(anselmo)
    grupo.adiciona(filha)
    return grupo


def testa_jogadores():
    grupo = monta_grupo_de_2()
    for _ in range(5):
        grupo.proximo()
        print('dix da vez', grupo.idx_da_vez)
        print('da vez', grupo.da_vez)


def testa_partida():
    grupo = monta_grupo_de_2()
    partida = Partida(grupo=grupo)
    partida.iniciar()


def main():
    testa_partida()


if __name__ == '__main__':
    # seed(42)
    main()
