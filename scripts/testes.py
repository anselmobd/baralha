from pprint import pprint
from random import seed, randint

from baralla.baralho import Baralho
from baralla.grupo import Grupo
from baralla.jogador import Jogador
from baralla.jogo import Jogo
from baralla.partida import Partida
from baralla.tipo_baralho import TipoBaralho
from baralla.tipo_jogo import TipoJogo


def testa_baralho():
    baralho = Baralho(TipoBaralho.ESPANHOL)
    baralho.embaralha()
    
    baralho.str_tudo(5)
    while baralho.monte:
        baralho.pega_carta()
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
    partida = Jogo(grupo=grupo)
    partida.iniciar()


def main():
    testa_partida()


if __name__ == '__main__':
    # seed(42)
    main()
