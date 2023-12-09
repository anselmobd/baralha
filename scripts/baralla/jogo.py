from pprint import pprint


class Jogo:
    def __init__(self, carac_jogo) -> None:
        self.carac_jogo = carac_jogo
        self.grupo = None

    def iniciar(self):
        print("iniciando jogo")
