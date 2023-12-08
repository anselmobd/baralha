from pprint import pprint


class TipoBaralho:

    def espanhol(self):
        self.naipes = {
            'O': 'ouros',
            'C': 'copas',
            'E': 'espadas',
            'P': 'paus',
        }
        self.cartas = {
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
        }
        return self

class Baralho:

    __ALEATORIA = 'aleatória'
    __ORDENADA = 'ordenada'

    def __init__(self, tipo = TipoBaralho().espanhol) -> None:
        self.tipo = tipo()
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
            for n in self.tipo.naipes
            for c in self.tipo.cartas
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







