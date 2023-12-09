from pprint import pprint

from baralla.tipo_baralho import TipoBaralho


class CustomTipoJogo:

    BRISCA = 'brisca'
    TESTE = 'teste'
    _JOGOS = {
        BRISCA: {
            'baralho': TipoBaralho.ESPANHOL,
            'número de jogadores': 2,  # 3 e 4 é possível, mas tem pequenas alterações nas regras
            'partida': {
                'num_jogos': 4,
            },
            'sentido jogadores': 'anti-horário',
            'primeiro crupier': 'jogador sorteado',
            'seguinte crupier': 'depois o próximo jogador',
            'preparação do jogo': (
                'crupier embaralha',
                'crupier distribui 3 cartas para cada jogador',
                'vira uma carta cujo naipe será o trunfo',
                'coloca a carta indicadora do trunfo aberta na mesa',
                'coloca o restante do baralho fechado na mesa, tampando metade da carta trunfo',  # que é assim considerada a última carta do monte
                'jogo começa pelo próximo jogador',
            ),
            'jogo': {
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
                    'sendo do mesmo naipe, as cartas tem uma ordem crescente de valor que define o ganhador da mão',
                ),
                'ordem crescente de valor das cartas na mão': (2, 3, 4, 5, 6, 7, 's', 'c', 'r', 3, 'a'),
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
                    'ás': 11,
                    '3': 10,
                    'rei': 4,
                    'cavalo': 3,
                    'sota': 2,
                },
                'pontos por naipe': 'não varia',
                'total de pontos no baralho': 120,
                'pontos de dobra': 100,
            },
            'pontuação na partida': (
                'ganha a partida quem ganhar 4 jogos primeiro',
            ),
        },
        TESTE: {
            'baralho': TipoBaralho.ESPANHOL,
            'número de jogadores': 2,
            'partida': {
                'num_jogos': 1,
            },
            'sentido jogadores': 'anti-horário',
            'crupier': 'externo',
            'preparação do jogo': (
                'crupier embaralha',
                'crupier distribui 3 cartas para cada jogador',
                'coloca o restante do baralho fechado na mesa',
                'jogo começa pelo próximo jogador',
            ),
            'jogo': {
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
                'ordem crescente de valor das cartas na mão': (2, 3, 4, 5, 6, 7, 's', 'c', 'r', 3, 'a'),
                'fim do ciclo': 'quando acabam as cartas nas mãos dos jogadores',
            },
            'finalização do jogo': (
                'cada jogador conta as cartas do seu monte de mãos ganhas no jogo',
                'quem tiver mais cartas no jogo, ganha o 1 jogo na partida',
                'se todos os jogadores empatarem, ninguem ganha 1 jogo',
            ),
            'pontuação na partida': (
                'ganha a partida o jogo',
            ),
        },
    }
