from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('livros/<int:id>/', views.livro_detalhe, name='livro_detalhe'),  # Nova rota para detalhes do livro
]
