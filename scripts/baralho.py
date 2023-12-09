from pprint import pprint
from random import seed, randint

from baralla.tipo_baralho import TipoBaralho
from baralla.tipo_jogo import TipoJogo


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


class Jogador:

    def __init__(self, nome) -> None:
        self.nome = nome

    def __str__(self) -> str:
        return self.nome


class Grupo:

    def __init__(self) -> None:
        self.jogadores = {}
        self._idx_da_vez = 0

    @property
    def num_jogadores(self):
        return len(self.jogadores)

    @property
    def da_vez(self):
        return self.jogadores.get(self._idx_da_vez, "")

    @property
    def idx_da_vez(self):
        return self._idx_da_vez

    def adiciona(self, jogador):
        self.jogadores[self.num_jogadores] = jogador

    def sorteia(self):
        self._idx_da_vez = randint(0, self.num_jogadores - 1)

    def proximo(self):
        self._idx_da_vez = (self._idx_da_vez + 1) % self.num_jogadores


class Partida:
    
    def __init__(self) -> None:
        pass


class Jogo:
    pass


def testa_baralho():
    baralho = Baralho(TipoBaralho.ESPANHOL)
    baralho.embaralha()
    
    baralho.str_tudo(5)
    while baralho.monte:
        baralho.vira_carta()
        baralho.str_tudo(5)


def testa_jogadores():
    anselmo = Jogador('Anselmo')
    alice = Jogador('Alice')

    grupo = Grupo()
    grupo.adiciona(anselmo)
    grupo.adiciona(alice)

    for _ in range(5):
        grupo.proximo()
        print('dix da vez', grupo.idx_da_vez)
        print('da vez', grupo.da_vez)


def main():
    testa_baralho()
    testa_jogadores()


if __name__ == '__main__':
    # seed(42)
    main()
