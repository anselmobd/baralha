import argparse
import sys
from pprint import pprint
from random import seed

from baralla.grupo import Grupo
from baralla.jogador import Jogador
from baralla.jogo import Jogo


def monta_grupo_de_2(logica_velha, logica_nova):
    velha = Jogador('Velha', logica_velha)
    nova = Jogador('Nova', logica_nova)
    grupo = Grupo()
    grupo.adiciona(velha)
    grupo.adiciona(nova)
    return grupo


def main(args):
    grupo = monta_grupo_de_2(args.velha, args.nova)
    jogo = Jogo('brisca2n', grupo)
    jogo.iniciar()


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
    parser.add_argument(
        '-v',
        '--velha',
        help="código da lógica da jogadora 'Velha'",
    )
    parser.add_argument(
        '-n',
        '--nova',
        help="código da lógica da jogadora 'Nova'",
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.seed:
        my_seed = args.seed
        seed(my_seed)
    main(args)
