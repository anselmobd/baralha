from pprint import pprint


class CustomTipoBaralho:

    TESTE = 'teste'
    ESPANHOL = 'espanhol'
    _NAIPE = {
        TESTE:
        {
            'o': 'ouros',
        },
        ESPANHOL:
        {
            'o': 'ouros',
            'c': 'copas',
            'e': 'espadas',
            'p': 'paus',
        },
    }
    _NUMERO_FIGURA = {
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
            'a': 'ás',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            's': 'sota',
            'c': 'cavalo',
            'r': 'rei',
        },
    }
