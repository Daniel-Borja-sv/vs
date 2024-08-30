"""
Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa
que lea la informacion basica del perro (no mas de 8 caracteristicas) y se muestren en pantalla. En esta
veterinaria todos los animales que llegan, entran con el estado inicial de NO ATENDIDO y cuando se 
registre se cambia automaticamente a ATENDIDO. por ahora como la veterinaria solo atiende a perros, 
basado en el peso,(menos de 10kg o mas 10kg) los registro como "perro grande" o "perro pequeño".

"""

class Perro:
    def __init__(self, nombre, edad, raza, peso, color, telefono):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.color = color
        self.telefono = telefono
        self.estado = "NO ATENDIDO"
        self.tamaño = "PERRO GRANDE" if peso >= 10 else "PERRO PEQUEÑO"


    def registrarperro(self):
        self.estado = "ATENDIDO"

    def mostrar_datos(self):
        print("***DATOS DEL PERRO***\n"+
            f"Nombre: {self.nombre}\n"+
            f"Edad: {self.edad}\n"+
            f"Raza: {self.raza}\n"+
            f"Peso: {self.peso} KG\n"+
            f"Color: {self.color}\n"+
            f"Telefono Del Dueño: {self.telefono}\n"+
            f"Estado: {self.estado}\n"+
            f"Tamaño: {self.tamaño}\n")
        
print("***VETERINARIA***\n")
nombre = input("Nombre del perro: ")
edad = int(input("Edad del perro: "))
raza = input("Raza del perro: ")
peso = float(input("Peso del perro (KG): "))
color = input("Color del perro: ")
telefono = int(input("Telefono del dueño: "))

perro = Perro(nombre, edad, raza, peso, color, telefono)
perro.registrarperro()
perro.mostrar_datos()
    
