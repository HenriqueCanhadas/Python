from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('data_criacao')[:5]
    return {"lista_filmes_recentes" : lista_filmes}