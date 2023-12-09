from pprint import pprint
from random import seed, randint


class TipoBaralho:

    TESTE = 'teste'
    ESPANHOL = 'espanhol'
    _NAIPES = {
        TESTE:
        {
            'O': 'ouros',
        },
        ESPANHOL:
        {
            'o': 'ouros',
            'c': 'copas',
            'e': 'espadas',
            'p': 'paus',
        },
    }
    _CARTAS = {
        TESTE:
        {
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': '10',
        },
        ESPANHOL:
        {
            'A': 'ás',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            'S': 'sota',
            'C': 'cavalo',
            'R': 'rei',
        },
    }

    def __init__(self, tipo=None) -> None:
        self.tipo = tipo if tipo else self.TESTE

    @property
    def naipes(self):
        return self._NAIPES[self.tipo]

    @property
    def cartas(self):
        return self._CARTAS[self.tipo]


class Baralho:

    __ALEATORIA = 'aleatória'
    __ORDENADA = 'ordenada'

    def __init__(self, tipo=None) -> None:
        self.tipo_baralho = TipoBaralho(tipo)
        self.ordena()
        
    def embaralha(self):
        self.ordem = self.__ALEATORIA
        self.inicializa_baralho()

    def ordena(self):
        self.ordem = self.__ORDENADA
        self.inicializa_baralho()

    def inicializa_baralho(self):
        self.monte = [
            (c, n)
            for n in self.tipo_baralho.naipes
            for c in self.tipo_baralho.cartas
        ]
        self.descarte = []
    
    def vira_carta(self):
        carta_idx = 0 if self.ordem == self.__ORDENADA else randint(0, len(self.monte)-1)
        self.descarte.append(self.monte[carta_idx])
        del(self.monte[carta_idx])

    def mostra_monte(self, n=0):
        self.mostra_cartas(self.monte, n)

    def mostra_descarte(self, n=0):
        self.mostra_cartas(self.descarte, n)

    def mostra_tudo(self, n=0):
        print('monte')
        self.mostra_cartas(self.monte, n)
        print('descarte')
        self.mostra_cartas(self.descarte, n)

    def get_cartas(self, cartas, n=0):
        result = []
        for i, carta in enumerate(cartas, start=1):
            result.append(carta)
            if i == n:
                break
        return result

    def mostra_cartas(self, cartas, n=0):
        for carta in self.get_cartas(cartas, n):
            pprint(carta)

    def str_tudo(self, n=0):
        print('monte', self.str_cartas(self.monte, n))
        print('descarte', self.str_cartas(self.descarte, n))

    def str_cartas(self, cartas, n=0):
        return "-".join(
            [f"{c}{n}" for c, n in self.get_cartas(cartas, n)]
        )


class Jogo:

    BRISCA = 'brisca'
    _JOGOS = {
        BRISCA: {
            'baralho': TipoBaralho.ESPANHOL,
            'partida': 'composta de vários jogos',
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
        }
    }


def main():
    baralho = Baralho(TipoBaralho.ESPANHOL)
    baralho.embaralha()
    
    while baralho.monte:
        baralho.str_tudo()
        baralho.vira_carta()
        baralho.str_tudo()


if __name__ == '__main__':
    seed(42)
    main()
