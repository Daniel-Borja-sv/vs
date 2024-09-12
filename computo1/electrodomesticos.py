"""
Una tienda vende 3 tipos de electrodomesticos, (refrigeradores, microondas y licuadoras). Todos los 
electrodomésticos son de una marca llamada "MABE". Cada producto tiene seis características 
principales que deben almacenarse, y su precio de venta se calcula con un margen de ganancia del 60% 
(multiplicado por 1.6).
"""

class ElectrodomesticoCocina:
    def __init__(self, tipo, modelo, capacidad, color, potencia, material, precio_compra):
        self.marca = "MABE"
        self.tipo = tipo  # Refrigerador, Microondas o Licuadora
        self.modelo = modelo
        self.capacidad = capacidad  # Capacidad (litros para refrigeradores, vatios para microondas/licuadoras)
        self.color = color
        self.potencia = potencia  # Potencia en vatios
        self.material = material  # Material de fabricación (por ejemplo, acero inoxidable)
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.6

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Color: {self.color}")
        print(f"Potencia: {self.potencia}W")
        print(f"Material: {self.material}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")

# Lista para almacenar los electrodomésticos
almacen = []

# Ejemplo de ingreso de electrodomésticos
electrodomestico1 = ElectrodomesticoCocina("Refrigerador", "mabe-Cool100", "300L", "Blanco", 150, "Acero Inoxidable", 800)
electrodomestico2 = ElectrodomesticoCocina("Microondas", "mabe-Micro50", "20L", "Negro", 700, "Plástico", 150)
electrodomestico3 = ElectrodomesticoCocina("Licuadora", "mabe-BlendX", "1.5L", "Rojo", 400, "Vidrio", 50)

# Agregar electrodomésticos al almacén
almacen.append(electrodomestico1)
almacen.append(electrodomestico2)
almacen.append(electrodomestico3)

# Mostrar la información de todos los electrodomésticos en el almacén
for electrodomestico in almacen:
    electrodomestico.mostrar_info()
    print("-" * 25)