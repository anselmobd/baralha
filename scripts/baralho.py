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
            'O': 'ouros',
            'C': 'copas',
            'E': 'espadas',
            'P': 'paus',
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


def main():
    baralho = Baralho()
    baralho.embaralha()
    
    while baralho.monte:
        baralho.str_tudo()
        baralho.vira_carta()
        baralho.str_tudo()


if __name__ == '__main__':
    seed(42)
    main()
