class Animal:
    def __init__(self, nombre, especie, edad, area):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.area = area
        self.tratamientos = []

    def agregar_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)

    def mostrar_tratamientos(self):
        if not self.tratamientos:
            print(f"{self.nombre} no tiene tratamientos en curso.")
        else:
            print(f"Tratamientos para {self.nombre}:")
            for tratamiento in self.tratamientos:
                print(f"  - {tratamiento}")

class Tratamiento:
    def __init__(self, medicamento, dosis, frecuencia):
        self.medicamento = medicamento
        self.dosis = dosis
        self.frecuencia = frecuencia

    def __str__(self):
        return f"{self.medicamento}, Dosis: {self.dosis}, Frecuencia: {self.frecuencia}"

class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        if not self.animales:
            print("No hay animales en el zoológico.")
        else:
            print("Animales en el zoológico:")
            for animal in self.animales:
                print(f"{animal.nombre} ({animal.especie}), {animal.edad} años, Área: {animal.area}")

    def listar_animales_en_tratamiento(self):
        print("Animales en tratamiento:")
        animales_en_tratamiento = [animal for animal in self.animales if animal.tratamientos]
        if not animales_en_tratamiento:
            print("No hay animales en tratamiento.")
        else:
            for animal in animales_en_tratamiento:
                print(f"{animal.nombre} ({animal.especie}):")
                animal.mostrar_tratamientos()

# Ejemplo de uso
zoologico = Zoologico()

# Crear algunos animales
leon = Animal("Simba", "León", 5, "Sabana")
tigre = Animal("Shere Khan", "Tigre", 8, "Selva")

# Agregar animales al zoológico
zoologico.agregar_animal(leon)
zoologico.agregar_animal(tigre)

# Crear tratamientos
tratamiento_leon = Tratamiento("Antibiótico", "500mg", "Cada 12 horas")
tratamiento_tigre = Tratamiento("Desparasitante", "300mg", "Cada 24 horas")

# Asignar tratamientos a los animales
leon.agregar_tratamiento(tratamiento_leon)
tigre.agregar_tratamiento(tratamiento_tigre)

# Listar animales y tratamientos
zoologico.listar_animales()
zoologico.listar_animales_en_tratamiento()