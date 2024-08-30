"""
un almacen vende dispositivos electronicos (celulares, tablets y portatiles), todos PHR que es una 
nueva marca que esta entrando en el mercado. Se requiere almacenar sus 6 principales caracteristicas.
todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 
que corresponde al margen de ganancia.
"""

class DispositivoElectronico:
    def __init__(self, tipo, modelo, color, almacenamiento, ram, procesador, precio_compra):
        self.marca = "PHR"  # los productos son de la marca PHR
        self.tipo = tipo  # Celular, Tablet o Portátil
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.procesador = procesador
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7
        self.importado = "SI"  # Todos los productos son importados



    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"RAM: {self.ram}")
        print(f"Procesador: {self.procesador}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print(f"Importado: {self.importado}")

# Lista para almacenar los dispositivos
almacen = []

# Ejemplo de ingreso de dispositivos
dispositivo1 = DispositivoElectronico("Celular", "PHR-500", "Negro", "128GB", "6GB", "Snapdragon 888", 300)
dispositivo2 = DispositivoElectronico("Tablet", "PHR-TabX", "Blanco", "256GB", "8GB", "M1", 500)
dispositivo3 = DispositivoElectronico("Portátil", "PHR-Laptop", "Gris", "512GB", "16GB", "Intel i7", 1000)

# Agregar dispositivos al almacén
almacen.append(dispositivo1)
almacen.append(dispositivo2)
almacen.append(dispositivo3)

# Mostrar la información de todos los dispositivos en el almacén
for dispositivo in almacen:
    dispositivo.mostrar_info()
    print("-" * 30)