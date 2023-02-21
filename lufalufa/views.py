from django.shortcuts import render
import fabrica

# Create your views here.


def salao_comunal(request):
    return render(request, 'lufalufa/pages/lufalufa.html')


def sobre(request):
    return render(request, 'lufalufa/pages/sobre_lufalufa.html')


def membros(request):
    return render(request, 'lufalufa/pages/membros_lufalufa.html')


def quadribol(request):
    return render(request, 'lufalufa/pages/quadribol_lufalufa.html', context={'trofeus': lista_vitorias})


lista_vitorias = [fabrica.jogo_lufalufa() for _ in range(10)]


def trofeu(request, id):
    for item in lista_vitorias:
        if item['ano'] == id:
            vitoria = item
            break
    return render(request, 'lufalufa/pages/trofeu.html',
                  context={'vitoria': vitoria})
