from django.shortcuts import render
import fabrica

# Create your views here.


def salao_comunal(request):
    return render(request, 'sonserina/pages/sonserina.html')


def sobre(request):
    return render(request, 'sonserina/pages/sobre_sonserina.html')


def membros(request):
    return render(request, 'sonserina/pages/membros_sonserina.html')


def quadribol(request):
    return render(request, 'sonserina/pages/quadribol_sonserina.html', context={'trofeus': lista_vitorias})


lista_vitorias = [fabrica.jogo_sonserina() for _ in range(10)]


def trofeu(request, id):
    for item in lista_vitorias:
        if item['ano'] == id:
            vitoria = item
            break
    return render(request, 'sonserina/pages/trofeu.html',
                  context={'vitoria': vitoria})
