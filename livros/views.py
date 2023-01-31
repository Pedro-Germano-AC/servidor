from django.shortcuts import render
from .models import Livro, Categoria
from django.contrib.auth.decorators import login_required 
from django.db.models import Q

@login_required(login_url='login:cadastro')
def home(request):
    q = request.GET.get('q1') if request.GET.get('q1') != None else ''
    pesquisa = True if request.GET.get('q1') != None and request.GET.get('q1') != '' else False
    livros = Livro.objects.filter(
        Q(Categoria__nome__icontains=q) |
        Q(Titulo__icontains=q) |
        Q(Autor__icontains=q) |
        Q(Coautor__icontains=q)     
        )
    Categorias = Categoria.objects.all()
    livros_count = livros.count()
    categorias_count = Categorias.count()

    context = {'livros':livros, 'Categorias':Categorias, 'livros_count': livros_count, 'pesquisa':pesquisa, 'categorias_count': categorias_count}
    return render(request, 'livros/Home_page.html',context)