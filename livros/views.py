from django.shortcuts import render
from .models import Livro, Categoria
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@login_required(login_url='login:cadastro')
def home(request):
    q = request.GET.get('q1') if request.GET.get('q1') != None else ''
    pesquisa = True if request.GET.get('q1') != None and request.GET.get('q1') != '' else False
    livros = Livro.objects.filter(
        Q(Categoria__nome__icontains=q) |
        Q(Titulo__icontains=q) |
        Q(Autores__icontains=q)     
        )
    Categorias = Categoria.objects.all()
    livros_count = livros.count()
    categorias_count = Categorias.count()

    context = {'livros':livros, 'Categorias':Categorias, 'livros_count': livros_count, 'pesquisa':pesquisa, 'categorias_count': categorias_count}
    return render(request, 'livros/Home_page.html',context)

def enviar_email_emprestimo(nome_usuario, email_usuario, nome_livro, data_devolucao, data_limite):
    mail_subject = "Confirmação de empréstimo PEToteca"
    message = render_to_string("livros/Confirmação_Emprestimo.html", {
        "nome_do_usuario": nome_usuario,
        "nome_do_livro": nome_livro,
        "data_de_devolucao": data_devolucao,
        "data_limite_recebimento": data_limite
    })
    to_email = email_usuario
    email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
    email.attach_alternative(message, "text/html")
    email.attach_file("livros\static\livros\Horário de Atendimento - Sala do PET 2022.png")
    email.send()
