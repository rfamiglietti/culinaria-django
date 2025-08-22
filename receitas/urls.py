from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Esta é a linha que você precisa adicionar ou corrigir
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'), 
    path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
]