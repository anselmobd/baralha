from pprint import pprint


class TipoBaralho:

    ESPANHOL = 'espanhol'
    _NAIPES = {
        ESPANHOL:
        {
            'O': 'ouros',
            'C': 'copas',
            'E': 'espadas',
            'P': 'paus',
        },
    }
    _CARTAS = {
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
        self.tipo = tipo if tipo else self.ESPANHOL

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
            (n, c)
            for n in self.tipo_baralho.naipes
            for c in self.tipo_baralho.cartas
        ]
    
    def mostra_monte(self, n=0):
        self.mostra(self.monte, n)

    def mostra(self, cartas, n=0):
        for i, carta in enumerate(cartas, start=1):
            pprint(carta)
            if i == n:
                break


if __name__ == '__main__':
    baralho = Baralho()
    baralho.mostra_monte(9)







