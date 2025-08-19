from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'receitas/home.html')

def receita_detail(request, receita_id):
    # Placeholder for recipe detail view logic
    context = {
        'receita_id': id,
        'receita_title': f'Receita Detalhada {id}', 
        'receita_description': f'Descrição detalhada da receita com id {id}.',
    }