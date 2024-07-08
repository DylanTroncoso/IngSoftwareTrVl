from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informacion', views.informacion, name='informacion'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('register-login/', views.register_login, name='register_login'),
    path('lista_servicios/', views.lista_servicios, name='lista_servicios'),
    path('agregar_producto/<int:idServicio>/', views.agregar_producto, name='agregar_producto'),
]
