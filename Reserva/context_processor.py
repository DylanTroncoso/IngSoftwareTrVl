
def total_carrito(request):
    total = 0
    if request.user in request.session:
        try:
            for key, value in request.session['reserva'].items():
                total = total + (int(value['precio']))*(value['cantidad'])
        except:
            request.session['reserva'] = {}
            total = 0
    return {"total_carrito":int(total)}

