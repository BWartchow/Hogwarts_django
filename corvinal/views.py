from django.shortcuts import render
import fabrica

# Create your views here.


def salao_comunal(request):
    return render(request, 'corvinal/pages/corvinal.html')


def sobre(request):
    return render(request, 'corvinal/pages/sobre_corvinal.html')


def membros(request):
    return render(request, 'corvinal/pages/membros_corvinal.html')


def quadribol(request):
    return render(request, 'corvinal/pages/quadribol_corvinal.html', context={'trofeus': lista_vitorias})


lista_vitorias = [fabrica.jogo_corvinal() for _ in range(10)]


def trofeu(request, id):
    for item in lista_vitorias:
        if item['ano'] == id:
            vitoria = item
            break
    return render(request, 'corvinal/pages/trofeu.html',
                  context={'vitoria': vitoria})
