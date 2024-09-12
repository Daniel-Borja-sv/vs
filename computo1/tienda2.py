#Creamos una clase llamada Producto
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

#creamos una clase llamada Tienda que nos va a permitir agregar y registrar las ventas
class Tienda:
    def __init__(self):
        self.inventario = {}

    #aqui utilizamos metodos que nos permitiran gestionar el como se agregan y se registran los productos
    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.inventario:
            self.inventario[nombre].cantidad += cantidad
        else:
            self.inventario[nombre] = Producto(nombre, cantidad, precio)
        print(f"Producto {nombre} agregado/actualizado con éxito.")
        print("-" * 30)

    def registrar_venta(self, nombre, cantidad, pago_cliente):
        if nombre not in self.inventario:
            print("Producto no encontrado en el inventario.")
            return
        producto = self.inventario[nombre]
        if cantidad > producto.cantidad:
            print("No hay suficiente cantidad en el inventario para realizar esta venta.")
            return

        total = producto.precio * cantidad
        cambio = pago_cliente - total

        if cambio < 0:
            print(f"El cliente no ha proporcionado suficiente dinero. Falta: ${-cambio:.2f}\n")
            return

        producto.cantidad -= cantidad
        print(f"Venta realizada con éxito. Total a pagar: ${total:.2f}. Cambio a devolver: ${cambio:.2f}")

    def consultar_inventario(self):
        print("Inventario actual:")
        for nombre, producto in self.inventario.items():
            print(f"Producto: {nombre}, Cantidad: {producto.cantidad}, Precio: ${producto.precio:.2f}")


tienda = Tienda()

# Registrar productos
tienda.agregar_producto("Manzanas", 50, 0.5)
tienda.agregar_producto("Bananas", 100, 0.3)
tienda.agregar_producto("Mango", 200, 0.7)


# Consultar inventario
tienda.consultar_inventario()

# Registrar venta
tienda.registrar_venta("Manzanas", 10, 10)  # Cliente compra 10 manzanas y paga con 10$
tienda.registrar_venta("Bananas", 101, 20)
tienda.registrar_venta("Mango", 35, 1)

# Consultar inventario después de la venta
tienda.consultar_inventario()