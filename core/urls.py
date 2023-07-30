from django.urls import path
from . import views

urlpatterns = [
    # Página inicial - exibirá o conteúdo de index.html
    path('', views.index, name='index'),
]