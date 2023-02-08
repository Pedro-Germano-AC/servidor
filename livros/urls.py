from django.urls import path

from . import views

app_name = 'livros'
urlpatterns = [

    path('', views.home, name="home-page"),
    path('Detalhes_livros',views.detalhes_livros, name="Detalhes_livros")
]