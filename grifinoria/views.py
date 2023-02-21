from django.shortcuts import render
import fabrica

# Create your views here.


def salao_comunal(request):
    return render(request, 'grifinoria/pages/grifinoria.html')


def sobre(request):
    return render(request, 'grifinoria/pages/sobre_grifinoria.html')


def membros(request):
    return render(request, 'grifinoria/pages/membros_grifinoria.html')


def quadribol(request):
    return render(request, 'grifinoria/pages/quadribol_grifinoria.html', context={'trofeus': lista_vitorias})


lista_vitorias = [fabrica.jogo_grifinoria() for _ in range(10)]


def trofeu(request, id):
    for item in lista_vitorias:
        if item['ano'] == id:
            vitoria = item
            break
    return render(request, 'grifinoria/pages/trofeu.html',
                  context={'vitoria': vitoria})
