# Definimos una clase para representar cada producto en la tienda
class Producto:
    def __init__(self, nombre, precio_venta, cantidad_disponible=0):
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.cantidad_disponible = cantidad_disponible

    def agregar_stock(self, cantidad):
        self.cantidad_disponible += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
            return cantidad * self.precio_venta
        else:
            print(f"No hay suficiente stock de {self.nombre}")
            return 0

# Creamos una clase para manejar la tienda
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio_venta, cantidad):
        producto = Producto(nombre, precio_venta, cantidad)
        self.productos.append(producto)
        print(f"Producto {nombre} agregado con {cantidad} en stock a {precio_venta} por unidad.")

    def registrar_proveedor(self, nombre, cantidad, precio_sugerido):
        # Busca si el producto ya existe en la tienda
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.agregar_stock(cantidad)
                producto.precio_venta = precio_sugerido
                print(f"Proveedor registrado. {nombre} actualizado con {cantidad} adicionales a {precio_sugerido} por unidad.")
                return
        # Si no existe, se agrega como un nuevo producto
        self.agregar_producto(nombre, precio_sugerido, cantidad)

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                total = producto.vender(cantidad)
                if total > 0:
                    print(f"Venta realizada. Total a pagar por {cantidad} de {nombre} es {total:.2f}")
                return total
        print(f"Producto {nombre} no encontrado.")
        return 0

    def calcular_vuelto(self, total, pago_cliente):
        if pago_cliente < total:
            print("El pago del cliente es insuficiente.")
            return -1
        vuelto = pago_cliente - total
        print(f"El vuelto del cliente es: {vuelto:.2f}")
        return vuelto

    def mostrar_inventario(self):
        print("Inventario de la tienda:")
        for producto in self.productos:
            print(f"{producto.nombre}: {producto.cantidad_disponible} unidades disponibles a {producto.precio_venta:.2f} cada una.")

# Código de ejecución
tienda = Tienda()

# Registrar productos de proveedores
tienda.registrar_proveedor("Manzanas", 50, 1.5)
tienda.registrar_proveedor("Leche", 30, 0.99)

# Vender productos a clientes
total_a_pagar = tienda.vender_producto("Manzanas", 5)
vuelto = tienda.calcular_vuelto(total_a_pagar, 10)  # El cliente paga con 10

# Mostrar inventario
tienda.mostrar_inventario()