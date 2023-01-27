from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.cadastroPage, name='cadastro'),
    path('logout/', views.logoutUser, name='logout'),
    path('ativar/<uidb64>/<token>', views.ativar, name='ativar'),
]