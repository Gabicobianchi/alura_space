from django.shortcuts import render


#Criando uma nova função - requisição
def index(request):
    return render(request, 'galeria/index.html')


def imagem(request):   
    return render(request, 'galeria/imagem.html')