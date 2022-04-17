from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/?P<nombre>\w+', views.detalle, name='detalle'),
    path('paginacion/?<pagina>', views.paginacion, name='paginacion'),
]