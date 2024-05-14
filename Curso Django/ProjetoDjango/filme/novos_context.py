from .models import Filme

def lista_filmes_recentes(request):
    # Lista os 10 filmes mais recentes
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:10]
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_emalta(request):
    # Lista os 10 filmes com mais visualizações
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:10]
    return {"lista_filmes_emalta": lista_filmes}

def filme_destaque(request):
    # Pega o filme mais recente como destaque
    filme = Filme.objects.order_by('-data_criacao').first()
    return {"filme_destaque": filme}