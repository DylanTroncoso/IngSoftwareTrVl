
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito
    
    def agregar(self, servicio):
        if servicio.idServicio not in self.carrito.keys():
            self.carrito[servicio.idServicio]={
                "servicio_id":servicio.idServicio, 
                "nombre": servicio.modelo,
                "precio": str (servicio.precio),
                "descripcion": servicio.descripcion,
                "cantidad": 1,
                "total": servicio.precio,

                }
        else:
            for key, value in self.carrito.items():
                if key==servicio.idServicio:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = servicio.precio
                    value["total"]= value["total"] + servicio.precio
                    break
        self.guardar_carrito()


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, servicio):
        id = servicio.idServicio
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,servicio):
        for key, value in self.carrito.items():
            if key == servicio.idServicio:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- servicio.precio
                if value["cantidad"] < 1:   
                    self.eliminar(servicio)
                break
        self.guardar_carrito()
        
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
