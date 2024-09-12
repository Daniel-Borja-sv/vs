"""
Un concesionario de autos vende vehiculos nacionales e importados. todos tienen 4 ruedas y capacidad 
para 5 pasajeros. esta informacion debe registrarse siempre por razones de ley. Requiere un programa
que le permita almacenar las 10 principales caracteristicas de los autos. El precio de de venta de cada
auto es igual al precio de compra multiplicado por 1.4 que corresponde a su margen de ganancia.
"""

class Auto:
    def __init__(self, marca, modelo, año, color, tipo, motor, transmision, combustible, kilometraje, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo  # Nacional o Importado
        self.motor = motor
        self.transmision = transmision
        self.combustible = combustible
        self.kilometraje = kilometraje
        self.precio_compra = precio_compra
        self.ruedas = 4  # Por ley, todos los autos tienen 4 ruedas
        self.capacidad_pasajeros = 5  # Por ley, todos los autos tienen capacidad para 5 pasajeros
        self.precio_venta = precio_compra * 1.4
   

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Combustible: {self.combustible}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")

# Lista para almacenar los autos
concesionario = []

# Ejemplo de ingreso de autos
auto1 = Auto("Toyota", "Corolla", 2021, "Blanco", "Nacional", "1.8L", "Automática", "Gasolina", 10000, 20000)
auto2 = Auto("Honda", "Civic", 2022, "Negro", "Importado", "2.0L", "Manual", "Gasolina", 5000, 25000)

# Agregar autos al concesionario
concesionario.append(auto1)
concesionario.append(auto2)

# Mostrar la información de todos los autos en el concesionario
for auto in concesionario:
    auto.mostrar_info()
    print("-" * 30)