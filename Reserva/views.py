from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, authenticate
from Reserva.models import Boleta, Servicio, detalle_boleta
from Reserva.reservas import Carrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm, SignUpForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def informacion(request):
    return render(request, 'informacion.html')

def catalogo(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'catalogo.html', context)

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'catalogo.html', {'servicio': servicios})

def login_register(request):
    return render(request, 'registration/login_register.html')

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    servicio = Servicio.objects.get(idServicio=id)
    carrito_compra.agregar(servicio=servicio)
    return redirect('catalogo')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    servicio = Servicio.objects.get(idServicio=id)
    carrito_compra.eliminar(servicio=servicio)
    return redirect('catalogo')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    servicio = Servicio.objects.get(idServicio=id)
    carrito_compra.restar(servicio=servicio)
    return redirect('catalogo')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('catalogo')


def register_login(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            signup_form = SignUpForm(request.POST)
            login_form = LoginForm()
            if signup_form.is_valid():
                user = signup_form.save()
                username = signup_form.cleaned_data.get('username')
                raw_password = signup_form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            login_form = LoginForm(request, data=request.POST)
            signup_form = SignUpForm()
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('home')
    else:
        signup_form = SignUpForm()
        login_form = LoginForm()
    
    return render(request, 'registration/register_login.html', {'signup_form': signup_form, 'login_form': login_form})


def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total=precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Servicio.objects.get(idServicio=value['servicio_id'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = detalle_boleta(id_boleta=boleta, id_producto=producto, cantidad=cant, subtotal=subtotal)
        detalle.save()
        productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total':boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html', datos)