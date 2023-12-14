import argparse
import sys
from pprint import pprint
from random import seed

from baralla.grupo import Grupo
from baralla.jogador import Jogador
from baralla.jogo import Jogo


def monta_grupo_de_2():
    velha = Jogador('Velha', '0.11.3')
    nova = Jogador('Nova', '0.12.0.treino')

    grupo = Grupo()
    grupo.adiciona(velha)
    grupo.adiciona(nova)
    return grupo


def testa_jogo():
    grupo = monta_grupo_de_2()
    jogo = Jogo('brisca2n', grupo)
    jogo.iniciar()


def main():
    testa_jogo()

def parse_args():
    parser = argparse.ArgumentParser(
        description=f"Executa Jogo",
    )
    parser.add_argument(
        '-s',
        '--seed',
        help="Sementa da aleatoriedade",
        type=int,
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.seed:
        my_seed = args.seed
        seed(my_seed)
    main()
