from pprint import pprint
from random import randint


class Logica:

    def __init__(self, jogo_def, versao) -> None:
        self.jogo_def = jogo_def
        self.versao = versao
        self.VERSOES = {
            '0.10.0': self.v0_10_0,
            '0.10.1': self.v0_10_1,
            '0.11.0': self.v0_11_0,
            '0.11.1': self.v0_11_1,
            '0.11.2': self.v0_11_2,
        }

    def executa(self, mesa, mao):
        return self.VERSOES[self.versao](mesa, mao)

    def v0_10_0(self, mesa, mao):
        """Sorteia uma carta"""
        return randint(0, len(mao)-1)

    def v0_10_1(self, mesa, mao):
        """Pega a primeira carta recebida"""
        return 0

    def minha_carta_melhor_que_a_da_mesa(self, mesa, mao):
        regua_valor = self.jogo_def['partida']['regua de valor dos números das cartas da mesa']
        mesa_naipe = mesa.cartas[0]['carta'].naipe
        mesa_numero = mesa.cartas[0]['carta'].numero
        mesa_valor = regua_valor.index(mesa_numero)
        carta_idx = -1
        carta_melhor_valor = -1
        for idx, carta in enumerate(mao):
            if carta.naipe == mesa_naipe:
                carta_valor = regua_valor.index(carta.numero)
                if carta_valor > mesa_valor and carta_valor > carta_melhor_valor:
                    carta_melhor_valor = carta_valor
                    carta_idx = idx
        return carta_idx


    def v0_11_0(self, mesa, mao):
        """
        Como primeiro: sorteia uma carta
        Como segundo: escolhe carta maior que a da mesa, se tiver, senão sorteia
        """
        if mesa.cartas:
            idx = self.minha_carta_melhor_que_a_da_mesa(mesa, mao)
            if idx > -1:
                return idx
        return self.v0_10_0(mesa, mao)

    def minha_carta_de_menor_valor(self, mesa, mao, sobre_trunfo=0):
        """
        Busca na mão a carta de menor valor com a seguinte condição com relação ao trunfo
        - sobre_trunfo == 1: a carta tem que ser trunfo
        - sobre_trunfo == 0: não se importa com naipe
        - sobre_trunfo == -1: a carta não pode ser trunfo
        Caso não encopntre o que procura, procura novamente sem se importar com o naipe
        """
        regua_valor = self.jogo_def['partida']['regua de valor dos números das cartas da mesa']
        trunfo_naipe = mesa.trunfo.naipe
        carta_idx = -1
        carta_menor_valor = 99
        for idx, carta in enumerate(mao):
            carta_valor = regua_valor.index(carta.numero)
            if (
                (
                    sobre_trunfo == 0 or
                    (sobre_trunfo == -1 and carta.naipe != trunfo_naipe) or
                    (sobre_trunfo == 1 and carta.naipe == trunfo_naipe)
                ) and
                carta_valor < carta_menor_valor
            ):
                carta_menor_valor = carta_valor
                carta_idx = idx
        if carta_idx == -1 and sobre_trunfo != 0:
            carta_idx = self.minha_carta_de_menor_valor(mesa, mao, sobre_trunfo=0)
        return carta_idx

    def v0_11_1(self, mesa, mao):
        """
        Como primeiro: escolhe carta de menor valor
        Como segundo: escolhe carta maior que a da mesa, se tiver,
            senão escolhe carta de menor valor
        """
        if mesa.cartas:
            idx = self.minha_carta_melhor_que_a_da_mesa(mesa, mao)
            if idx > -1:
                return idx
        return self.minha_carta_de_menor_valor(mesa, mao)

    def v0_11_2(self, mesa, mao):
        """
        Como primeiro: escolhe carta de menor valor, não trunfo, se possível
        Como segundo:
            Se a carta da mesa é um trunfo, joga como se fosse o primeiro
            Senão,
                Escolhe carta maior que a da mesa, se tiver
                Senão tiver,
                    Se a carta vale pontos, escolhe carta trunfo de menor valor, se possível
                    Senão, joga como se fosse o primeiro
        """
        if mesa.cartas:
            trunfo_naipe = mesa.trunfo.naipe
            mesa_naipe = mesa.cartas[0]['carta'].naipe
            arrastou = mesa_naipe == trunfo_naipe

            pontos = self.jogo_def['pontos no jogo']['pontos das cartas']
            mesa_numero = mesa.cartas[0]['carta'].numero
            jogou_pontos = mesa_numero in pontos.keys()

            if arrastou:
                idx = self.minha_carta_de_menor_valor(mesa, mao, sobre_trunfo=-1)
            else:
                idx = self.minha_carta_melhor_que_a_da_mesa(mesa, mao)
                if idx > -1:
                    return idx
                if jogou_pontos:
                    idx = self.minha_carta_de_menor_valor(mesa, mao, sobre_trunfo=1)
            if idx > -1:
                return idx
        return self.minha_carta_de_menor_valor(mesa, mao, sobre_trunfo=-1)
