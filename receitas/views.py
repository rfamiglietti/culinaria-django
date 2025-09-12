from django.shortcuts import render
from .models import Receita  # Certifique-se de que Receita está importado

def home(request, categoria_slug=None):
    # Verifica se um slug de categoria foi passado na URL
    if categoria_slug:
        # Se houver um slug, define a categoria selecionada e filtra as receitas
        categoria_selecionada = categoria_slug
        receitas = Receita.objects.filter(categoria__slug=categoria_slug)
    else:
        # Se não houver slug, define um valor padrão e mostra todas as receitas
        categoria_selecionada = 'all'  # Use uma string mais amigável, como 'todas'
        receitas = Receita.objects.all()

    # Define as opções de categorias, ou pegue-as do seu modelo se houver
    categorias_choices = ['comida', 'sobremesa', 'drink']

    context = {
        'receitas': receitas,
        'categoria_selecionada': categoria_selecionada,
        'categorias_choices': categorias_choices,
    }
    
    return render(request, 'home.html', context)

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

def pesquisar_receitas(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Receita.objects.filter(title__icontains=query)
    return render(request, 'receitas/pesquisa.html', {
        'query': query,
        'receitas': resultados
    })

