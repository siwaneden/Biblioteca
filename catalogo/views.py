from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'catalogo/lista_livros.html', {'livros': livros})

def adicionar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'catalogo/adicionar_livro.html', {'form': form})

def livro_detalhe(request, id):
    try:
        livro = Livro.objects.get(id=id)
        return JsonResponse({
            'id': livro.id,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'isbn': livro.isbn,
            'resumo': livro.resumo
        })
    except Livro.DoesNotExist:
        return JsonResponse({'error': 'Livro não encontrado'}, status=404)
