from random import randint


def jogo_grifinoria():
    times = ['grifinoria', 'lufalufa', 'sonserina', 'corvinal']
    fotos = ['../../../static/grifinoria/imgs/quadribol_logo.jpg',
             '../../../static/grifinoria/imgs/quadribol_poster.jpg', '../../../static/grifinoria/imgs/quadribol_taca.jpg']
    foto = randint(0, 2)
    indice = randint(1, 3)
    return {
        'jogo': f'{times[0]} X {times[indice]}',
        'descricao': 'Lorem ipsum dolor sit amet consectetur sit maxime ducimus quidem minus nihil unde, ipsam, quo tempora ea!',
        'ano': randint(1499, 2023),
        'foto': f'{fotos[foto]}'
    }


def jogo_sonserina():
    times = ['sonserina', 'grifinoria', 'lufalufa', 'corvinal']
    fotos = ['../../../static/sonserina/imgs/quadribol_logo.jpg',
             '../../../static/sonserina/imgs/quadribol_poster.jpg', '../../../static/sonserina/imgs/quadribol_taca.jpg']
    foto = randint(0, 2)
    indice = randint(1, 3)
    return {
        'jogo': f'{times[0]} X {times[indice]}',
        'descricao': 'Lorem ipsum dolor sit amet consectetur sit maxime ducimus quidem minus nihil unde, ipsam, quo tempora ea!',
        'ano': randint(1499, 2023),
        'foto': f'{fotos[foto]}'
    }


def jogo_corvinal():
    times = ['corvinal', 'sonserina', 'grifinoria', 'lufalufa']
    fotos = ['../../../static/corvinal/imgs/quadribol_logo.jpg',
             '../../../static/corvinal/imgs/quadribol_poster.jpg', '../../../static/corvinal/imgs/quadribol_taca.jpg']
    foto = randint(0, 2)
    indice = randint(1, 3)
    return {
        'jogo': f'{times[0]} X {times[indice]}',
        'descricao': 'Lorem ipsum dolor sit amet consectetur sit maxime ducimus quidem minus nihil unde, ipsam, quo tempora ea!',
        'ano': randint(1499, 2023),
        'foto': f'{fotos[foto]}'
    }


def jogo_lufalufa():
    times = ['lufalufa', 'corvinal', 'sonserina', 'grifinoria']
    fotos = ['../../../static/lufalufa/imgs/quadribol_logo.jpg',
             '../../../static/lufalufa/imgs/quadribol_poster.jpg', '../../../static/lufalufa/imgs/quadribol_taca.jpg']
    foto = randint(0, 2)
    indice = randint(1, 3)
    return {
        'jogo': f'{times[0]} X {times[indice]}',
        'descricao': 'Lorem ipsum dolor sit amet consectetur sit maxime ducimus quidem minus nihil unde, ipsam, quo tempora ea!',
        'ano': randint(1499, 2023),
        'foto': f'{fotos[foto]}'
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(jogo_grifinoria())
