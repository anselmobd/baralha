from pprint import pprint

from baralla.tipo_baralho import TipoBaralho


class TipoJogoTeste:
    ID = 'teste'
    DEFINICAO = {
        'baralho': TipoBaralho.ESPANHOL,
        'número de jogadores': 2,
        'jogo': {
            'num_partidas': 1,
        },
        'sentido jogadores': 'anti-horário',
        'carteador': 'externo',
        'preparação da partida': {
            'passos': (
                'carteador embaralha',
                'carteador distribui n_cartas cartas para cada jogador',
                'coloca o restante do baralho fechado na mesa',
                'jogo começa pelo próximo jogador',
            ),
            'parâmetros': {
                'num_cartas': 3,
            }
        },
        'partida': {
            'ciclo': (
                'jogador da vez escolhe uma das cartas da mão e coloca aberta na mesa',
                'cada jogador faz o mesmo até cada jogador descartar uma carta',
                'sabendo a ordem das cartas e quem apresentou cada uma, é verificado o vencedor da mão',
                'o vencedor da mão recolhe as cartas da mesa e guarda fechadas em seu monte',
                'o vencedor da mão compra uma carta do monte, se ainda houver',
                'cada jogador faz o mesmo até cada jogador comprar uma carta, se houver',
                'o vencedor da mão é agora o jogador da vez',
            ),
            'avaliando o vencedor da mão': (
                'o naipe da primeira carta colocada na mesa em cada mão é o carro',
                'o naipe do carro ganha de todos os outros naipes',
                'sendo do mesmo naipe, as cartas tem uma ordem crescente de valor que define o ganhador da mão',
            ),
            'regua de valor dos números das cartas da mesa': ('2', '3', '4', '5', '6', '7', 's', 'c', 'r', '3', 'a'),
            'fim do ciclo': 'quando acabam as cartas nas mãos dos jogadores',
        },
        'finalização do jogo': (
            'cada jogador conta as cartas do seu monte de mãos ganhas no jogo',
            'quem tiver mais cartas no jogo, ganha o 1 jogo na partida',
            'se todos os jogadores empatarem, ninguem ganha 1 jogo',
        ),
        'pontos no jogo': {
            'pontos das cartas': {
                '2': 1,
                '3': 2,
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                's': 7,
                'c': 8,
                'r': 9,
                'a': 10,
            },
            'pontos por naipe': 'não varia',
        },
        'pontuação na partida': (
            'ganha a partida o jogo',
        ),
    }
