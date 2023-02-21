from django.shortcuts import render

# Create your views here.


def castelo(request):
    return render(request, 'castelo/pages/castelo.html')


def casas(request):
    return render(request, 'castelo/pages/casas.html')
