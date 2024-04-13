from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'recipes/home.html', context={
        'name': ' JONAS',
        })


def contato(request):
    return HttpResponse('Oi Contato')

def sobre(request):
    return HttpResponse('OI Sobre')