from pprint import pprint
from random import seed, randint

from baralla.baralho import Baralho
from baralla.grupo import Grupo
from baralla.jogador import Jogador
from baralla.jogo import Jogo
from baralla.partida import Partida
from baralla.tipo_baralho import TipoBaralho
from baralla.tipo_jogo import TipoJogo


def monta_grupo_de_2():
    velha = Jogador('Velha')
    nova = Jogador('Nova', '0.10.1')

    grupo = Grupo()
    grupo.adiciona(velha)
    grupo.adiciona(nova)
    return grupo


def testa_jogo():
    grupo = monta_grupo_de_2()
    jogo = Jogo('brisca', grupo)
    jogo.iniciar()


def main():
    testa_jogo()


if __name__ == '__main__':
    # seed(42)
    main()
