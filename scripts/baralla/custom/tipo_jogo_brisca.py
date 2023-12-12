from pprint import pprint

from baralla.tipo_baralho import TipoBaralho


class TipoJogoBrisca:
    ID = 'brisca'
    DEFINICAO = {
        'baralho': TipoBaralho.ESPANHOL,
        'número de jogadores': 2,  # 3 e 4 é possível, mas tem pequenas alterações nas regras
        'jogo': {
            'num_partidas': 1,  # 4,
        },
        'sentido jogadores': 'anti-horário',
        'primeiro carteador': 'jogador sorteado',
        'seguinte carteador': 'depois o próximo jogador',
        'preparação da partida': {
            'passos': (
                'carteador embaralha',
                'carteador distribui n_cartas cartas para cada jogador',
                'vira uma carta cujo naipe será o trunfo',
                'coloca a carta indicadora do trunfo aberta na mesa',
                'coloca o restante do baralho fechado na mesa, tampando metade da carta trunfo',  # que é assim considerada a última carta do monte
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
                'o naipe do carro ganha de todos os outros naipes, exceto do trunfo, que ganha de todos',
                'sendo do mesmo naipe, as cartas da mesa tem uma ordem crescente de valor que define o ganhador da mão',
            ),
            'regua de valor dos números das cartas da mesa': ('2', '3', '4', '5', '6', '7', 's', 'c', 'r', '3', 'a'),
            'fim do ciclo': 'quando acabam as cartas nas mãos dos jogadores',
        },
        'finalização do jogo': (
            'cada jogador conta os pontos das cartas do seu monte de mãos ganhas no jogo',
            'quem tiver mais pontos no jogo, ganha o 1 jogo na partida',
            'se todos os jogadores empatarem, ninguem ganha 1 jogo',
            'se alguém fizer os pontos de dobra ou mais, conta como 2 jogos',
        ),
        'pontos no jogo': {
            'pontos das cartas': {
                'a': 11,
                '3': 10,
                'r': 4,
                'c': 3,
                's': 2,
            },
            'pontos por naipe': 'não varia',
            'total de pontos no baralho': 120,
            'pontos de dobra': 100,
        },
        'pontuação na partida': (
            'ganha a partida quem ganhar 4 jogos primeiro',
        ),
    }
